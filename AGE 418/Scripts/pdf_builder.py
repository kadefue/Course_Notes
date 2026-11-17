import os
import zlib
import struct
import re

# Page geometry (US Letter)
PAGE_WIDTH = 612.0
PAGE_HEIGHT = 792.0
MARGIN_LEFT = 46.0
MARGIN_RIGHT = 46.0
MARGIN_TOP = 46.0
MARGIN_BOTTOM = 46.0
CONTENT_WIDTH = PAGE_WIDTH - MARGIN_LEFT - MARGIN_RIGHT

# Colors
C_SUA_GREEN = (0.0, 0.533, 0.212)      # #008836
C_SUA_DARKGREEN = (0.0, 0.353, 0.141)  # #005a24
C_TEXT = (0.12, 0.16, 0.22)            # #1f2937
C_MUTED = (0.35, 0.40, 0.47)           # #5b6777
C_BORDER = (0.80, 0.83, 0.86)          # #ccd3db
C_BG_LIGHT = (0.965, 0.98, 0.965)      # Light green tint
C_WHITE = (1.0, 1.0, 1.0)
C_BOX_GRAY = (0.95, 0.96, 0.97)

# Character widths for Helvetica
HELVETICA_WIDTHS = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, "'": 222,
    '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333, '.': 278, '/': 278,
    '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556, '7': 556,
    '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556,
    '@': 1015, 'A': 667, 'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778,
    'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778,
    'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556,
    '`': 222, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556,
    'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833, 'n': 556, 'o': 556,
    'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722,
    'x': 500, 'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584,
    '–': 556, '—': 1000, '“': 333, '”': 333, '‘': 222, '’': 222, '•': 350
}

def str_w(text, size, bold=False):
    factor = 1.05 if bold else 1.0
    return sum((HELVETICA_WIDTHS.get(c, 550) * size / 1000.0) * factor for c in text)

def escape_pdf(text):
    return text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')

def unfilter_png(data):
    w, h, depth, colortype = struct.unpack('>IIBB', data[16:26])
    assert depth == 8 and colortype == 6, 'Must be 8-bit RGBA'
    pos = 8
    idat = b''
    while pos < len(data):
        length, chunk_type = struct.unpack('>I4s', data[pos:pos+8])
        if chunk_type == b'IDAT':
            idat += data[pos+8:pos+8+length]
        pos += 12 + length
    raw = zlib.decompress(idat)
    stride = 1 + w * 4
    unfiltered = bytearray(w * h * 4)
    for y in range(h):
        filter_type = raw[y * stride]
        for x in range(w * 4):
            val = raw[y * stride + 1 + x]
            left = unfiltered[y * w * 4 + x - 4] if x >= 4 else 0
            up = unfiltered[(y - 1) * w * 4 + x] if y > 0 else 0
            left_up = unfiltered[(y - 1) * w * 4 + x - 4] if (x >= 4 and y > 0) else 0
            if filter_type == 0:
                pass
            elif filter_type == 1:
                val = (val + left) & 0xff
            elif filter_type == 2:
                val = (val + up) & 0xff
            elif filter_type == 3:
                val = (val + ((left + up) >> 1)) & 0xff
            elif filter_type == 4:
                p = left + up - left_up
                pa = abs(p - left)
                pb = abs(p - up)
                pc = abs(p - left_up)
                if pa <= pb and pa <= pc:
                    pr = left
                elif pb <= pc:
                    pr = up
                else:
                    pr = left_up
                val = (val + pr) & 0xff
            unfiltered[y * w * 4 + x] = val
    rgb = bytearray(w * h * 3)
    alpha = bytearray(w * h)
    for i in range(w * h):
        rgb[i*3] = unfiltered[i*4]
        rgb[i*3+1] = unfiltered[i*4+1]
        rgb[i*3+2] = unfiltered[i*4+2]
        alpha[i] = unfiltered[i*4+3]
    return w, h, bytes(rgb), bytes(alpha)

class PDFBuilder:
    def __init__(self, logo_path):
        self.pages = []  # list of command lists
        self.cur_cmds = []
        self.y = PAGE_HEIGHT - MARGIN_TOP
        self.page_num = 1
        with open(logo_path, 'rb') as f:
            self.img_w, self.img_h, self.img_rgb, self.img_alpha = unfilter_png(f.read())
        self.start_page()

    def start_page(self):
        self.cur_cmds = []
        self.y = PAGE_HEIGHT - MARGIN_TOP
        if self.page_num > 1:
            # Running header
            # Mini logo at top left
            logo_w = 20
            logo_h = 20
            logo_x = MARGIN_LEFT
            logo_y = PAGE_HEIGHT - 36
            self.cur_cmds.append(f"q {logo_w} 0 0 {logo_h} {logo_x} {logo_y} cm /ImLogo Do Q")
            # Text next to logo
            self.cur_cmds.append(f"BT /F2 8.5 Tf {C_SUA_GREEN[0]} {C_SUA_GREEN[1]} {C_SUA_GREEN[2]} rg {MARGIN_LEFT + 26} {PAGE_HEIGHT - 28} Td (SOKOINE UNIVERSITY OF AGRICULTURE) Tj ET")
            self.cur_cmds.append(f"BT /F1 7.5 Tf {C_TEXT[0]} {C_TEXT[1]} {C_TEXT[2]} rg {MARGIN_LEFT + 26} {PAGE_HEIGHT - 37} Td (Department of Agricultural Engineering | EPAL) Tj ET")
            # Course & assignment right-aligned
            course_text = "AGE 418: Practical Assignment 1 (2026/2027)"
            w_course = str_w(course_text, 8, bold=True)
            self.cur_cmds.append(f"BT /F2 8 Tf {C_SUA_DARKGREEN[0]} {C_SUA_DARKGREEN[1]} {C_SUA_DARKGREEN[2]} rg {PAGE_WIDTH - MARGIN_RIGHT - w_course} {PAGE_HEIGHT - 32} Td ({escape_pdf(course_text)}) Tj ET")
            # Header line
            self.cur_cmds.append(f"{C_SUA_GREEN[0]} {C_SUA_GREEN[1]} {C_SUA_GREEN[2]} RG 0.8 w {MARGIN_LEFT} {PAGE_HEIGHT - 44} m {PAGE_WIDTH - MARGIN_RIGHT} {PAGE_HEIGHT - 44} l S")
            self.y = PAGE_HEIGHT - 58
        else:
            self.y = PAGE_HEIGHT - MARGIN_TOP

    def check_space(self, need_height):
        if self.y - need_height < MARGIN_BOTTOM + 25:
            self.pages.append(self.cur_cmds)
            self.page_num += 1
            self.start_page()

    def draw_text(self, text, x, y, font="F1", size=9, color=C_TEXT):
        self.cur_cmds.append(f"BT /{font} {size} Tf {color[0]} {color[1]} {color[2]} rg {x} {y} Td ({escape_pdf(text)}) Tj ET")

    def draw_line(self, x1, y1, x2, y2, color=C_BORDER, width=0.5):
        self.cur_cmds.append(f"{color[0]} {color[1]} {color[2]} RG {width} w {x1} {y1} m {x2} {y2} l S")

    def draw_rect(self, x, y, w, h, fill=None, stroke=None, stroke_width=0.5):
        cmds = []
        if fill:
            cmds.append(f"{fill[0]} {fill[1]} {fill[2]} rg")
        if stroke:
            cmds.append(f"{stroke[0]} {stroke[1]} {stroke[2]} RG {stroke_width} w")
        op = "B" if (fill and stroke) else ("f" if fill else "S")
        cmds.append(f"{x} {y} {w} {h} re {op}")
        self.cur_cmds.append(" ".join(cmds))

    def add_spacer(self, h):
        self.y -= h

    def add_first_page_header(self):
        # Draw SUA Logo centered at top
        logo_size = 54
        logo_x = (PAGE_WIDTH - logo_size) / 2.0
        logo_y = self.y - logo_size
        self.cur_cmds.append(f"q {logo_size} 0 0 {logo_size} {logo_x} {logo_y} cm /ImLogo Do Q")
        self.y = logo_y - 12

        # Titles
        univ = "SOKOINE UNIVERSITY OF AGRICULTURE"
        uw = str_w(univ, 14, bold=True)
        self.draw_text(univ, (PAGE_WIDTH - uw) / 2.0, self.y, font="F2", size=14, color=C_SUA_GREEN)
        self.y -= 14

        school = "SCHOOL OF ENGINEERING AND TECHNOLOGY"
        sw = str_w(school, 10.5, bold=True)
        self.draw_text(school, (PAGE_WIDTH - sw) / 2.0, self.y, font="F2", size=10.5, color=C_TEXT)
        self.y -= 13

        dept = "DEPARTMENT OF AGRICULTURAL ENGINEERING"
        dw = str_w(dept, 9.5, bold=True)
        self.draw_text(dept, (PAGE_WIDTH - dw) / 2.0, self.y, font="F2", size=9.5, color=C_MUTED)
        self.y -= 13

        acad = "ACADEMIC YEAR 2026/2027"
        aw = str_w(acad, 9, bold=True)
        self.draw_text(acad, (PAGE_WIDTH - aw) / 2.0, self.y, font="F2", size=9, color=C_SUA_GREEN)
        self.y -= 8

        # Green divider
        self.draw_line(MARGIN_LEFT, self.y, PAGE_WIDTH - MARGIN_RIGHT, self.y, color=C_SUA_GREEN, width=1.5)
        self.y -= 14

        # Course & Assignment Banner
        course = "AGE 418: SENSORS AND CONTROLS FOR PRECISION AGRICULTURE"
        cw = str_w(course, 12, bold=True)
        self.draw_text(course, (PAGE_WIDTH - cw) / 2.0, self.y, font="F2", size=12, color=C_SUA_DARKGREEN)
        self.y -= 15

        asn = "PRACTICAL ASSIGNMENT 1"
        asnw = str_w(asn, 13, bold=True)
        self.draw_text(asn, (PAGE_WIDTH - asnw) / 2.0, self.y, font="F2", size=13, color=C_SUA_GREEN)
        self.y -= 12

        # Metadata Box
        box_lines = [
            ("Assignment Title: ", "Integrated Sentinel-1 and Sentinel-2 Remote Sensing for Assessing Seasonal Cropping Patterns, Vegetation Dynamics, and Climate–Crop Interactions in Kondoa and Bahi Districts, Dodoma Region, Tanzania (2016–2026)."),
            ("Study Area: ", "Kondoa and Bahi Districts, Dodoma Region, Tanzania."),
            ("Target Degree Programs: ", "BSc in Agricultural Engineering & BSc in Irrigation and Water Resources Engineering (Year 4)."),
            ("Submission Channel: ", "Individual GitHub Repository (Invited Collaborator: @kadefue)."),
            ("Submission Deadline: ", "8 December 2026.")
        ]
        
        # Calculate box height
        box_w = CONTENT_WIDTH
        wrapped_meta = []
        for label, val in box_lines:
            full = label + val
            w_label = str_w(label, 8.5, bold=True)
            # wrap value
            words = val.split()
            cur_line = []
            lines_for_entry = []
            for word in words:
                cur_line.append(word)
                prefix_w = w_label if len(lines_for_entry) == 0 else 0
                if prefix_w + str_w(" ".join(cur_line), 8.5) > (box_w - 20):
                    cur_line.pop()
                    lines_for_entry.append(" ".join(cur_line))
                    cur_line = [word]
            if cur_line:
                lines_for_entry.append(" ".join(cur_line))
            wrapped_meta.append((label, lines_for_entry))
        
        total_meta_lines = sum(len(lines) for _, lines in wrapped_meta)
        box_h = 16 + total_meta_lines * 11
        
        # Draw box
        box_y = self.y - box_h
        self.draw_rect(MARGIN_LEFT, box_y, box_w, box_h, fill=C_BG_LIGHT, stroke=C_SUA_GREEN, stroke_width=1.0)
        
        text_y = self.y - 14
        for label, m_lines in wrapped_meta:
            for idx, m_line in enumerate(m_lines):
                if idx == 0:
                    self.draw_text(label, MARGIN_LEFT + 10, text_y, font="F2", size=8.5, color=C_SUA_DARKGREEN)
                    w_l = str_w(label, 8.5, bold=True)
                    self.draw_text(m_line, MARGIN_LEFT + 10 + w_l, text_y, font="F1", size=8.5, color=C_TEXT)
                else:
                    self.draw_text(m_line, MARGIN_LEFT + 10, text_y, font="F1", size=8.5, color=C_TEXT)
                text_y -= 11
            text_y -= 2
        
        self.y = box_y - 12

    def add_h1(self, text):
        self.check_space(28)
        self.y -= 6
        # Background bar
        bar_h = 17
        self.draw_rect(MARGIN_LEFT, self.y - bar_h + 3, CONTENT_WIDTH, bar_h, fill=C_SUA_GREEN)
        self.draw_text(text, MARGIN_LEFT + 8, self.y - 10, font="F2", size=10, color=C_WHITE)
        self.y -= (bar_h + 6)

    def add_h2(self, text):
        self.check_space(20)
        self.y -= 4
        self.draw_text(text, MARGIN_LEFT, self.y - 8, font="F2", size=9.5, color=C_SUA_DARKGREEN)
        self.draw_line(MARGIN_LEFT, self.y - 11, MARGIN_LEFT + str_w(text, 9.5, bold=True) + 15, self.y - 11, color=C_SUA_GREEN, width=0.8)
        self.y -= 18

    def add_h3(self, text):
        self.check_space(16)
        self.y -= 2
        self.draw_text(text, MARGIN_LEFT + 4, self.y - 7, font="F2", size=9, color=C_TEXT)
        self.y -= 13

    def add_paragraph(self, text, indent=0, bold_prefix="", italic=False):
        font = "F3" if italic else "F1"
        size = 8.5
        line_h = 11.5
        
        # Format bold prefix if any
        prefix_w = str_w(bold_prefix, size, bold=True) if bold_prefix else 0
        avail_w = CONTENT_WIDTH - indent
        
        words = text.split()
        lines = []
        cur = []
        first_line = True
        
        for w in words:
            cur.append(w)
            p_w = prefix_w if first_line else 0
            if p_w + str_w(" ".join(cur), size) > avail_w:
                cur.pop()
                if cur:
                    lines.append(" ".join(cur))
                cur = [w]
                first_line = False
        if cur:
            lines.append(" ".join(cur))
            
        needed = len(lines) * line_h + 3
        self.check_space(needed)
        
        for idx, line in enumerate(lines):
            cur_y = self.y - 8
            if idx == 0 and bold_prefix:
                self.draw_text(bold_prefix, MARGIN_LEFT + indent, cur_y, font="F2", size=size, color=C_SUA_DARKGREEN)
                self.draw_text(line, MARGIN_LEFT + indent + prefix_w, cur_y, font=font, size=size, color=C_TEXT)
            else:
                self.draw_text(line, MARGIN_LEFT + indent, cur_y, font=font, size=size, color=C_TEXT)
            self.y -= line_h
        self.y -= 2

    def add_bullet(self, text, bold_prefix=""):
        self.add_paragraph(text, indent=14, bold_prefix="• " + bold_prefix)

    def add_numbered(self, num_str, text, bold_prefix=""):
        self.add_paragraph(text, indent=16, bold_prefix=num_str + " " + bold_prefix)

    def add_callout(self, title, text):
        words = text.split()
        lines = []
        cur = []
        box_w = CONTENT_WIDTH
        avail_w = box_w - 20
        for w in words:
            cur.append(w)
            if str_w(" ".join(cur), 8.5) > avail_w:
                cur.pop()
                lines.append(" ".join(cur))
                cur = [w]
        if cur:
            lines.append(" ".join(cur))
        
        box_h = 22 + len(lines) * 11
        self.check_space(box_h + 6)
        
        box_y = self.y - box_h
        self.draw_rect(MARGIN_LEFT, box_y, box_w, box_h, fill=C_BOX_GRAY, stroke=C_BORDER, stroke_width=0.8)
        self.draw_rect(MARGIN_LEFT, box_y, 3.5, box_h, fill=C_SUA_GREEN)
        
        self.draw_text(title, MARGIN_LEFT + 10, self.y - 12, font="F2", size=9, color=C_SUA_DARKGREEN)
        text_y = self.y - 23
        for l in lines:
            self.draw_text(l, MARGIN_LEFT + 10, text_y, font="F1", size=8.5, color=C_TEXT)
            text_y -= 11
            
        self.y = box_y - 8

    def finalize(self):
        self.pages.append(self.cur_cmds)
        total_pages = len(self.pages)
        
        # Add footers to all pages
        for p_idx in range(total_pages):
            cmds = self.pages[p_idx]
            p_num = p_idx + 1
            # Footer rule
            cmds.append(f"{C_BORDER[0]} {C_BORDER[1]} {C_BORDER[2]} RG 0.5 w {MARGIN_LEFT} {MARGIN_BOTTOM + 16} m {PAGE_WIDTH - MARGIN_RIGHT} {MARGIN_BOTTOM + 16} l S")
            # Left footer
            cmds.append(f"BT /F1 7.5 Tf {C_MUTED[0]} {C_MUTED[1]} {C_MUTED[2]} rg {MARGIN_LEFT} {MARGIN_BOTTOM + 6} Td (AGE 418: Practical Assignment 1 | Sokoine University of Agriculture) Tj ET")
            # Center footer
            dead_str = "Deadline: 8 December 2026"
            dw = str_w(dead_str, 7.5)
            cmds.append(f"BT /F2 7.5 Tf {C_SUA_DARKGREEN[0]} {C_SUA_DARKGREEN[1]} {C_SUA_DARKGREEN[2]} rg {(PAGE_WIDTH - dw)/2.0} {MARGIN_BOTTOM + 6} Td ({dead_str}) Tj ET")
            # Right footer
            p_str = f"Page {p_num} of {total_pages}"
            pw = str_w(p_str, 7.5)
            cmds.append(f"BT /F1 7.5 Tf {C_TEXT[0]} {C_TEXT[1]} {C_TEXT[2]} rg {PAGE_WIDTH - MARGIN_RIGHT - pw} {MARGIN_BOTTOM + 6} Td ({p_str}) Tj ET")
        
        return self.pages

    def build_pdf_bytes(self):
        pages_cmds = self.finalize()
        num_pages = len(pages_cmds)
        
        pdf = bytearray()
        pdf.extend(b"%PDF-1.4\n")
        pdf.extend(b"%\xe2\xe3\xcf\xd3\n")
        
        offsets = {}
        next_id = 1
        
        def start_obj():
            nonlocal next_id
            obj_id = next_id
            next_id += 1
            offsets[obj_id] = len(pdf)
            pdf.extend(f"{obj_id} 0 obj\n".encode('ascii'))
            return obj_id
            
        def end_obj():
            pdf.extend(b"\nendobj\n")
            
        # Catalog: obj 1
        cat_id = start_obj()
        pdf.extend(f"<< /Type /Catalog /Pages 2 0 R >>".encode('ascii'))
        end_obj()
        
        # Pages object will be obj 2
        pages_id = start_obj()
        # placeholder, write later
        
        # Font 1: Helvetica
        f1_id = start_obj()
        pdf.extend(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>")
        end_obj()
        
        # Font 2: Helvetica-Bold
        f2_id = start_obj()
        pdf.extend(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>")
        end_obj()
        
        # Font 3: Helvetica-Oblique
        f3_id = start_obj()
        pdf.extend(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique /Encoding /WinAnsiEncoding >>")
        end_obj()
        
        # Image Alpha SMask
        smask_id = start_obj()
        comp_alpha = zlib.compress(self.img_alpha)
        pdf.extend(f"<< /Type /XObject /Subtype /Image /Width {self.img_w} /Height {self.img_h} /ColorSpace /DeviceGray /BitsPerComponent 8 /Filter /FlateDecode /Length {len(comp_alpha)} >>\nstream\n".encode('ascii'))
        pdf.extend(comp_alpha)
        pdf.extend(b"\nendstream")
        end_obj()
        
        # Image RGB with SMask
        img_id = start_obj()
        comp_rgb = zlib.compress(self.img_rgb)
        pdf.extend(f"<< /Type /XObject /Subtype /Image /Width {self.img_w} /Height {self.img_h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /SMask {smask_id} 0 R /Filter /FlateDecode /Length {len(comp_rgb)} >>\nstream\n".encode('ascii'))
        pdf.extend(comp_rgb)
        pdf.extend(b"\nendstream")
        end_obj()
        
        page_ids = []
        for p_idx, cmds in enumerate(pages_cmds):
            content_stream = "\n".join(cmds).encode('utf-8')
            comp_content = zlib.compress(content_stream)
            
            # Content stream obj
            stream_id = start_obj()
            pdf.extend(f"<< /Length {len(comp_content)} /Filter /FlateDecode >>\nstream\n".encode('ascii'))
            pdf.extend(comp_content)
            pdf.extend(b"\nendstream")
            end_obj()
            
            # Page obj
            p_obj_id = start_obj()
            page_ids.append(p_obj_id)
            pdf.extend(f"<< /Type /Page /Parent {pages_id} 0 R /MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] /Resources << /Font << /F1 {f1_id} 0 R /F2 {f2_id} 0 R /F3 {f3_id} 0 R >> /XObject << /ImLogo {img_id} 0 R >> >> /Contents {stream_id} 0 R >>".encode('ascii'))
            end_obj()
            
        # Rewrite Pages obj at pages_id
        kids_str = " ".join(f"{pid} 0 R" for pid in page_ids)
        pages_content = f"<< /Type /Pages /Kids [{kids_str}] /Count {num_pages} >>"
        # Overwrite in buffer
        # In this simple builder, we can append it properly by creating it before or using indirect
        # Let's fix offsets for pages_id
        offsets[pages_id] = len(pdf)
        pdf.extend(f"{pages_id} 0 obj\n{pages_content}\nendobj\n".encode('ascii'))
        
        # Cross reference table
        xref_offset = len(pdf)
        total_objs = next_id
        pdf.extend(f"xref\n0 {total_objs}\n".encode('ascii'))
        pdf.extend(b"0000000000 65535 f \n")
        for i in range(1, total_objs):
            off = offsets[i]
            pdf.extend(f"{off:010d} 00000 n \n".encode('ascii'))
            
        pdf.extend(f"trailer\n<< /Size {total_objs} /Root {cat_id} 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode('ascii'))
        return bytes(pdf)

print('PDFBuilder class compiled successfully')
