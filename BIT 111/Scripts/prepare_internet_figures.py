#!/usr/bin/env python3
"""Prepare Wikimedia image assets and verified reuse credits for BIT 111."""

import json
import shutil
from pathlib import Path
from urllib.parse import quote

FIGURES_DIR = Path(__file__).resolve().parents[1] / "Figures" / "Internet"
MANIFEST_PATH = FIGURES_DIR / "attributions.json"

SOURCE_FILES = {
    1: [
        "Abacus actually in use at kimono shop in Otaru.jpg",
        "Arthur Burks, with a section of the ENIAC computer.jpg",
        "19-NN-AGM-10 General Vadenburg-NAID6929976.jpg",
        "255-GRC-1983-C-01769.jpg",
        "AlbanyStateUniversity ComputerOperationsRoom 1981 3 skaliert.jpg",
        "BRL61-0892.jpg",
        "Control Console of Univac 1830 Computer.jpg",
        "Charles-babbage.jpg",
    ],
    2: [
        "286 AT motherboard.jpg",
        "A80386DX-25 SX218.jpg",
        "Amstrad VSC386SXD V2.01.jpg",
        "Atari-800-Motherboard-Flat-Top.jpg",
        "Athlon II.JPG",
        "Camera zoom burst on a Microsoft computer keyboard in Tuntorp 8.jpg",
        "New 3D workstation using recycled parts over 5-10 years old - Dual Core AMD Opteron@1.2GHz,2GB RAM, ATI R350, dual display@2560x1024. CentOS 5.3 with prop. ATI driver. M-Audio Fast Track USB (2005-01-12 05.06.35 by Lee Azzarello).jpg",
        "Personal computer, exploded.svg",
    ],
    3: [
        "Computer locked.jpg",
        "Data security privacy lock password (41237924492).jpg",
        "Example bank phishing email.svg",
        "Example phishing SMS.svg",
        "Firewall.png",
        "National Cyber Security Awareness Month.jpg",
        "Security token.jpg",
        "SmartScreen warning in Internet Explorer 10.png",
    ],
    4: [
        "Desktop Linux Mint 9 KDE.png",
        "Ekran görüntüsü 2021-08-20 15-05-42.png",
        "Linux-Mint-MATE-20-desktop.png",
        "Computer Science lab, at block 247 lab 293 at the University of Botswana.jpg",
        "De La Salle University – Dasmariñas (DLSU–D) Information and Communications Technology Center (ICTC) laboratory room 203 (ICT203) — normal view.jpg",
        "Computer lab showing desktop PCs warwick.jpg",
        "Arch Linux system update via pacman on an Acer laptop.jpg",
        "Desktop computer system diagram (English).svg",
    ],
    5: [
        "Closeup of Excel Spreadsheet template to track printouts (29911005444).jpg",
        "Excel chart.PNG",
        "Fungsi Proper Pada Microsoft Excel.png",
        "Libreoffice-calc.png",
        "LibreOffice 7.2.4.1 Calc with csv screenshot.png",
        "SUM formula in LibreOffice Calc.png",
        "Mozilla Thunderbird 140 ESR on Debian 13 (Trixie) and KDE Plasma 6.png",
        "CPT 8100 Word Processor Desktop Microcomputer 5185A65A.png",
    ],
    6: [
        "AIDS DOS Trojan.png",
        "Computer locked.jpg",
        "Data security privacy lock password (41237924492).jpg",
        "Example bank phishing email.svg",
        "Example phishing SMS.svg",
        "Firewall.png",
        "National Cyber Security Awareness Month.jpg",
        "Security token.jpg",
    ],
}

CREDITS = {
    "Abacus actually in use at kimono shop in Otaru.jpg": ("Syced", "CC0"),
    "Arthur Burks, with a section of the ENIAC computer.jpg": ("University of Michigan. News and Information Services.", "CC BY 4.0"),
    "19-NN-AGM-10 General Vadenburg-NAID6929976.jpg": ("Department of Defense. Department of the Navy. Bureau of Ships.", "Public domain"),
    "255-GRC-1983-C-01769.jpg": ("Unknown author", "Public domain"),
    "AlbanyStateUniversity ComputerOperationsRoom 1981 3 skaliert.jpg": ("Erick M. Griffin", "Public domain"),
    "BRL61-0892.jpg": ("U. S. Army Chemical Corps Proving Ground (Dugway)", "Public domain"),
    "Control Console of Univac 1830 Computer.jpg": ("LaserSam", "CC BY-SA 4.0"),
    "Charles-babbage.jpg": ("Enslin (original uploader, German Wikipedia)", "Public domain"),
    "286 AT motherboard.jpg": ("Mister rf", "CC BY-SA 4.0"),
    "A80386DX-25 SX218.jpg": ("Mister rf", "CC BY-SA 4.0"),
    "Amstrad VSC386SXD V2.01.jpg": ("Mister rf", "CC BY-SA 4.0"),
    "Atari-800-Motherboard-Flat-Top.jpg": ("Evan-Amos", "Public domain"),
    "Athlon II.JPG": ("Chrihern", "Public domain"),
    "Camera zoom burst on a Microsoft computer keyboard in Tuntorp 8.jpg": ("W.carter", "CC BY-SA 4.0"),
    "New 3D workstation using recycled parts over 5-10 years old - Dual Core AMD Opteron@1.2GHz,2GB RAM, ATI R350, dual display@2560x1024. CentOS 5.3 with prop. ATI driver. M-Audio Fast Track USB (2005-01-12 05.06.35 by Lee Azzarello).jpg": ("Lee Azzarello", "CC BY-SA 2.0"),
    "Personal computer, exploded.svg": ("Gustavb", "CC BY 2.5"),
    "Computer locked.jpg": ("Juan Pablo Olmo", "CC BY 2.0"),
    "Data security privacy lock password (41237924492).jpg": ("Book Catalog", "CC BY 2.0"),
    "Example bank phishing email.svg": ("Original template by User:Isochrone, amended by User:Belbury", "CC BY 4.0"),
    "Example phishing SMS.svg": ("Belbury", "CC0"),
    "Firewall.png": ("Bruno Pedrozo", "CC BY-SA 3.0"),
    "National Cyber Security Awareness Month.jpg": ("National Science Foundation", "Public domain"),
    "Security token.jpg": ("cryptocard", "CC BY 3.0"),
    "SmartScreen warning in Internet Explorer 10.png": ("Brent Geuens", "CC0"),
    "Desktop Linux Mint 9 KDE.png": ("SteefuitHeerlen", "CC BY 3.0"),
    "Ekran görüntüsü 2021-08-20 15-05-42.png": ("AliIsingor", "CC BY-SA 4.0"),
    "Linux-Mint-MATE-20-desktop.png": ("Michal Stanke", "CC BY-SA 4.0"),
    "Computer Science lab, at block 247 lab 293 at the University of Botswana.jpg": ("Sikolethu", "CC BY-SA 4.0"),
    "De La Salle University – Dasmariñas (DLSU–D) Information and Communications Technology Center (ICTC) laboratory room 203 (ICT203) — normal view.jpg": ("UndueMarmot", "CC0"),
    "Computer lab showing desktop PCs warwick.jpg": ("User Mike1024 on English Wikipedia", "Public domain"),
    "Arch Linux system update via pacman on an Acer laptop.jpg": ("Solijon Solayev", "CC BY-SA 4.0"),
    "Desktop computer system diagram (English).svg": ("Photograph: kjarrett on Flickr", "CC BY 2.0"),
    "Closeup of Excel Spreadsheet template to track printouts (29911005444).jpg": ("Texas State Library and Archives Commission from Austin, TX, United States", "CC BY 2.0"),
    "Excel chart.PNG": ("Brews ohare", "Public domain"),
    "Fungsi Proper Pada Microsoft Excel.png": ("Umulhidayah", "CC BY-SA 4.0"),
    "Libreoffice-calc.png": ("The Document Foundation and Canonical", "CC0"),
    "LibreOffice 7.2.4.1 Calc with csv screenshot.png": ("The Document Foundation, Alessandro Ghedini, Matthias C. Hormann, and contributors; screenshot: VulcanSphere", "MPL 2"),
    "SUM formula in LibreOffice Calc.png": ("Arlo Barnes", "CC0"),
    "Mozilla Thunderbird 140 ESR on Debian 13 (Trixie) and KDE Plasma 6.png": ("Victor Matheus Amaral", "CC0"),
    "CPT 8100 Word Processor Desktop Microcomputer 5185A65A.png": ("LehmanUMN", "CC0"),
    "AIDS DOS Trojan.png": ("Joseph L. Popp, AIDS Information Trojan author", "Public domain"),
}


def license_url(license_name):
    if license_name == "CC0":
        return "https://creativecommons.org/publicdomain/zero/1.0/"
    if license_name.startswith("CC BY-SA "):
        version = license_name.removeprefix("CC BY-SA ")
        return f"https://creativecommons.org/licenses/by-sa/{version}/"
    if license_name.startswith("CC BY "):
        version = license_name.removeprefix("CC BY ")
        return f"https://creativecommons.org/licenses/by/{version}/"
    if license_name == "MPL 2":
        return "https://www.mozilla.org/en-US/MPL/2.0/"
    return ""


def source_page(filename):
    return "https://commons.wikimedia.org/wiki/File:" + quote(
        filename.replace(" ", "_"), safe=":/()'-,."
    )


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    available = {}
    for topic in range(1, 6):
        for index, filename in enumerate(SOURCE_FILES[topic], start=1):
            matches = list(FIGURES_DIR.glob(f"topic_{topic}_{index:02d}.*"))
            if len(matches) != 1:
                raise FileNotFoundError(
                    f"Expected one downloaded image for Topic {topic}, figure {index}; "
                    "download the image from its Wikimedia Commons file page."
                )
            available.setdefault(filename, matches[0])
    topic_six_first = list(FIGURES_DIR.glob("topic_6_01.*"))
    if len(topic_six_first) == 1:
        available["AIDS DOS Trojan.png"] = topic_six_first[0]

    manifest = {}
    for topic, filenames in SOURCE_FILES.items():
        manifest[str(topic)] = []
        for index, filename in enumerate(filenames, start=1):
            source_path = available.get(filename)
            if source_path is None:
                raise FileNotFoundError(f"No downloaded Commons asset for {filename}")
            output_name = f"topic_{topic}_{index:02d}{source_path.suffix.lower()}"
            output_path = FIGURES_DIR / output_name
            if source_path != output_path and not output_path.is_file():
                shutil.copyfile(source_path, output_path)
            creator, license_name = CREDITS[filename]
            manifest[str(topic)].append({
                "filename": output_name,
                "title": filename,
                "description": Path(filename).stem.replace("_", " "),
                "creator": creator,
                "license": license_name,
                "license_url": license_url(license_name),
                "source_url": source_page(filename),
            })

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Prepared 48 Wikimedia Commons figures with creator/license credits.")
    print(f"Saved attributions to {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
