import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)
from pdf_builder import PDFBuilder

base_dir = os.path.abspath(os.path.join(script_dir, "..", ".."))
logo_path = os.path.join(base_dir, "SUA.png")

builder = PDFBuilder(logo_path)
builder.add_first_page_header()

# SECTION 1
builder.add_h1("1. ASSIGNMENT QUESTION")
builder.add_paragraph(
    "Using Google Earth Engine (GEE), Geographic Information Systems (GIS), satellite remote sensing, and climate datasets, "
    "conduct a comprehensive spatiotemporal assessment of agricultural cropping patterns, vegetation dynamics, and climate "
    "variability in Kondoa and Bahi Districts, Dodoma Region, Tanzania, covering the period 2016–2026."
)
builder.add_paragraph(
    "The study must integrate Sentinel-1 Synthetic Aperture Radar (SAR), Sentinel-2 Multispectral Imagery, CHIRPS rainfall data, "
    "and ERA5-Land temperature data to investigate seasonal agricultural activities, vegetation conditions, crop development, "
    "rainfall variability, temperature dynamics, and vegetation recovery following rainfall and dry periods."
)
builder.add_paragraph("Your analysis should address the following seven (7) core research components:")

builder.add_spacer(4)

# 1.1
builder.add_h2("1.1 Study Area Characterisation and Mapping")
builder.add_numbered("1.", "Obtain administrative boundary data from the National Bureau of Statistics (NBS), Tanzania.")
builder.add_numbered("2.", "Extract and map Kondoa and Bahi Districts, showing their respective ward boundaries.")
builder.add_numbered("3.", "Characterise the geographical and administrative distribution of the study area.")
builder.add_numbered("4.", "Produce detailed district-level and ward-level maps with appropriate cartographic elements, including legends, scale bars, north arrows, coordinate systems, and data sources.")
builder.add_numbered("5.", "Calculate the geographical area of each district and ward where appropriate.")

builder.add_spacer(4)

# 1.2
builder.add_h2("1.2 Satellite and Climate Data Acquisition and Preprocessing")
builder.add_paragraph("Acquire, process, and analyse the following datasets using Google Earth Engine:")

builder.add_h3("A. Sentinel-1 Synthetic Aperture Radar (SAR)")
builder.add_paragraph("Use Sentinel-1 Ground Range Detected (GRD) imagery to:")
builder.add_bullet("Extract VV and VH polarization backscatter.")
builder.add_bullet("Analyse VV/VH and VH/VV backscatter ratios.")
builder.add_bullet("Investigate temporal changes in radar backscatter.")
builder.add_bullet("Generate appropriate radar-based vegetation indicators.")
builder.add_bullet("Examine crop development, vegetation structure, and surface moisture conditions.")
builder.add_bullet("Apply appropriate filtering, orbit selection, speckle reduction, and temporal compositing techniques.")

builder.add_h3("B. Sentinel-2 Multispectral Imagery")
builder.add_paragraph("Use Sentinel-2 Level-2A Surface Reflectance imagery to:")
builder.add_bullet("Apply cloud and cloud-shadow masking.")
builder.add_bullet("Extract relevant visible, red-edge, near-infrared, and shortwave-infrared bands.")
builder.add_bullet("Generate monthly, seasonal, and annual satellite composites.")
builder.add_bullet("Calculate vegetation indices relevant to agricultural monitoring.")
builder.add_bullet("Investigate crop establishment, development, peak growth, and vegetation decline.")

builder.add_h3("C. CHIRPS Rainfall Data")
builder.add_paragraph("Use Climate Hazards Group InfraRed Precipitation with Station Data (CHIRPS) to:")
builder.add_bullet("Estimate daily, monthly, seasonal, and annual rainfall.")
builder.add_bullet("Analyse rainfall distribution and spatial variability.")
builder.add_bullet("Identify rainfall onset and cessation.")
builder.add_bullet("Identify dry spells and rainfall deficits.")
builder.add_bullet("Investigate interannual and seasonal rainfall variability.")

builder.add_h3("D. ERA5-Land Temperature Data")
builder.add_paragraph("Use ERA5-Land to:")
builder.add_bullet("Extract 2 m air temperature.")
builder.add_bullet("Calculate monthly, seasonal, and annual temperature statistics.")
builder.add_bullet("Examine mean, minimum, and maximum temperature conditions using appropriate temporal aggregations.")
builder.add_bullet("Analyse seasonal and interannual temperature variability.")
builder.add_bullet("Investigate potential relationships between temperature conditions and vegetation development.")
builder.add_paragraph("Note: Convert ERA5-Land temperature measurements from Kelvin to degrees Celsius before reporting results.", bold_prefix="Unit Conversion:")

builder.add_callout(
    "Data Temporal Coverage & Availability Notice (2016–2026):",
    "Use the period 2016–2026, subject to actual data availability. Clearly document the data acquisition dates and acknowledge that 2026 may represent an incomplete year at the time of analysis."
)

builder.add_spacer(4)

# 1.3
builder.add_h2("1.3 Vegetation Index Computation and Analysis")
builder.add_paragraph("Calculate and analyse important vegetation indices using Sentinel-2 imagery. Consider the following indices and explain their relevance to agricultural monitoring:")

builder.add_h3("A. General Vegetation Greenness and Crop Growth")
builder.add_numbered("1.", "Normalized Difference Vegetation Index (NDVI)")
builder.add_numbered("2.", "Enhanced Vegetation Index (EVI)")
builder.add_numbered("3.", "Two-Band Enhanced Vegetation Index (EVI2)")
builder.add_numbered("4.", "Green Normalized Difference Vegetation Index (GNDVI)")

builder.add_h3("B. Soil-Adjusted Vegetation Indices")
builder.add_numbered("5.", "Soil Adjusted Vegetation Index (SAVI)")
builder.add_numbered("6.", "Modified Soil Adjusted Vegetation Index (MSAVI2)")
builder.add_numbered("7.", "Optimized Soil Adjusted Vegetation Index (OSAVI)")

builder.add_h3("C. Chlorophyll and Crop Health Indices")
builder.add_numbered("8.", "Normalized Difference Red Edge Index (NDRE)")
builder.add_numbered("9.", "Chlorophyll Index Red Edge (CIred-edge)")
builder.add_numbered("10.", "MERIS Terrestrial Chlorophyll Index (MTCI)")

builder.add_h3("D. Vegetation Water Content and Moisture Stress Indices")
builder.add_numbered("11.", "Normalized Difference Moisture Index (NDMI)")
builder.add_numbered("12.", "Moisture Stress Index (MSI)")
builder.add_numbered("13.", "Normalized Difference Water Index (NDWI)")
builder.add_numbered("14.", "Modified Normalized Difference Water Index (MNDWI)")

builder.add_h3("E. Biomass, Vegetation Disturbance, and Productivity Indices")
builder.add_numbered("15.", "Normalized Burn Ratio (NBR)")
builder.add_numbered("16.", "Normalized Burn Ratio 2 (NBR2)")
builder.add_numbered("17.", "Near-Infrared Reflectance of Vegetation (NIRv)")
builder.add_numbered("18.", "Structure Insensitive Pigment Index (SIPI)")
builder.add_numbered("19.", "Visible Atmospherically Resistant Index (VARI)")

builder.add_h3("F. Sentinel-1 Radar-Derived Vegetation Indicators")
builder.add_numbered("20.", "Radar Vegetation Index (RVI), using an appropriate dual-polarization formulation")
builder.add_numbered("21.", "VV/VH backscatter ratio")
builder.add_numbered("22.", "VH/VV backscatter ratio")
builder.add_numbered("23.", "Temporal VV and VH backscatter change indicators")

builder.add_spacer(2)
builder.add_paragraph("Analytical Requirements & Scientific Rigor:", bold_prefix="Analysis Mandate: ")
builder.add_bullet("Calculate at least eight (8) relevant optical vegetation indices from Sentinel-2.")
builder.add_bullet("Calculate and analyse relevant radar indicators from Sentinel-1.")
builder.add_bullet("Explain the scientific purpose and agricultural relevance of each selected index.")
builder.add_bullet("Generate spatial maps and temporal profiles.")
builder.add_bullet("Compare the sensitivity of selected indices to vegetation greenness, soil background, chlorophyll, biomass, and moisture conditions.")
builder.add_bullet("Identify the indices that provide the most useful information for monitoring agricultural vegetation in the study area.")
builder.add_paragraph(
    "Ensure that the correct Sentinel-2 spectral bands are used for each index. Distinguish vegetation moisture indices "
    "from surface-water indices and explain any limitations associated with their interpretation."
)

builder.add_spacer(4)

# 1.4
builder.add_h2("1.4 Seasonal Cropping Patterns and Vegetation Dynamics")
builder.add_paragraph("Investigate agricultural vegetation dynamics across the Masika and Vuli agricultural seasons, considering their local applicability to the study area. Specifically:")
builder.add_bullet("Identify and characterise the seasonal cropping periods.")
builder.add_bullet("Analyse vegetation development during the two seasons.")
builder.add_bullet("Compare seasonal NDVI, EVI, SAVI, and other selected vegetation indices.")
builder.add_bullet("Identify the timing of vegetation emergence, peak greenness, and decline.")
builder.add_bullet("Assess spatial differences in vegetation conditions across Kondoa and Bahi.")
builder.add_bullet("Examine interannual changes in seasonal vegetation patterns between 2016 and 2026.")
builder.add_bullet("Identify areas exhibiting consistent, variable, or contrasting seasonal vegetation behaviour.")
builder.add_paragraph("Use both Sentinel-1 and Sentinel-2 observations to complement the seasonal assessment.")

builder.add_spacer(4)

# 1.5
builder.add_h2("1.5 Rainfall and Temperature Variability Analysis")
builder.add_paragraph("Integrate CHIRPS rainfall and ERA5-Land temperature datasets to investigate climatic conditions across the study area. The analysis should include:")
builder.add_bullet("Monthly, seasonal, and annual rainfall distribution.")
builder.add_bullet("Seasonal rainfall totals and anomalies.")
builder.add_bullet("Rainfall onset and cessation.")
builder.add_bullet("Dry-spell duration and frequency.")
builder.add_bullet("Monthly and seasonal temperature patterns.")
builder.add_bullet("Annual temperature variability and anomalies.")
builder.add_bullet("Spatial distribution of rainfall and temperature.")
builder.add_bullet("Comparison of climatic conditions between Kondoa and Bahi.")
builder.add_paragraph("Investigate how rainfall and temperature variability may influence agricultural vegetation development and seasonal cropping patterns.")

builder.add_spacer(4)

# 1.6
builder.add_h2("1.6 Vegetation Recovery, Crop Wilting, and Moisture Stress Assessment")
builder.add_paragraph("Investigate vegetation responses to rainfall events, prolonged dry periods, and changing temperature conditions. The analysis should:")
builder.add_bullet("Estimate vegetation recovery time following rainfall events and dry periods.")
builder.add_bullet("Identify periods of vegetation greenness decline.")
builder.add_bullet("Investigate possible crop wilting and vegetation moisture stress using appropriate satellite indicators.")
builder.add_bullet("Examine relationships between rainfall events, temperature conditions, and vegetation recovery.")
builder.add_bullet("Identify spatial differences in vegetation recovery and decline.")
builder.add_bullet("Compare vegetation responses using Sentinel-1 radar indicators and Sentinel-2 optical indices.")
builder.add_bullet("Assess whether vegetation recovery patterns differ between Masika and Vuli seasons.")
builder.add_paragraph("Clearly distinguish satellite-derived estimates of vegetation stress and recovery from direct field measurements of crop wilting.")

builder.add_spacer(4)

# 1.7
builder.add_h2("1.7 Integrated Climate–Vegetation and Precision Agriculture Assessment")
builder.add_paragraph("Integrate Sentinel-1, Sentinel-2, CHIRPS, and ERA5-Land datasets to investigate the relationships between climatic conditions and agricultural vegetation dynamics. Specifically:")
builder.add_bullet("Examine relationships between rainfall, temperature, and vegetation indices.")
builder.add_bullet("Investigate the response of vegetation indicators to rainfall variability.")
builder.add_bullet("Analyse possible temperature-related vegetation stress.")
builder.add_bullet("Compare radar and optical indicators of vegetation conditions.")
builder.add_bullet("Identify areas with contrasting vegetation development and recovery patterns.")
builder.add_bullet("Determine which satellite and climate indicators are most informative for agricultural monitoring.")
builder.add_bullet("Discuss how the findings could support precision agriculture, agricultural decision-making, and climate-informed crop management in Kondoa and Bahi.")
builder.add_paragraph(
    "Use appropriate statistical techniques, temporal analysis, correlation analysis, and spatial analysis to support your findings. "
    "Where appropriate, apply regression or other suitable analytical methods, ensuring that the methodology accounts for temporal "
    "dependence and avoids unsupported causal interpretations."
)

builder.add_spacer(6)

# SECTION 2
builder.add_h1("2. EXPECTED OUTPUTS AND DELIVERABLES")
builder.add_paragraph("Students are expected to produce the following ten (10) tangible deliverables:")
builder.add_numbered("1.", "District and ward-level administrative maps of Kondoa and Bahi.", bold_prefix="Study area maps: ")
builder.add_numbered("2.", "Processed Sentinel-1 and Sentinel-2 datasets.", bold_prefix="Satellite data products: ")
builder.add_numbered("3.", "Spatial maps and temporal profiles of at least eight optical vegetation indices and relevant radar-derived indicators.", bold_prefix="Vegetation index products: ")
builder.add_numbered("4.", "Comparative assessment of Masika and Vuli vegetation dynamics.", bold_prefix="Seasonal analysis: ")
builder.add_numbered("5.", "CHIRPS-derived rainfall maps, seasonal totals, anomalies, and temporal trends.", bold_prefix="Rainfall analysis: ")
builder.add_numbered("6.", "ERA5-Land-derived temperature maps, seasonal patterns, and temporal trends.", bold_prefix="Temperature analysis: ")
builder.add_numbered("7.", "Analysis of vegetation recovery, decline, and potential moisture stress.", bold_prefix="Vegetation recovery assessment: ")
builder.add_numbered("8.", "Statistical and spatial investigation of climate–vegetation relationships.", bold_prefix="Integrated analysis: ")
builder.add_numbered("9.", "At least 10 high-quality figures, tables, and maps collectively presenting the major findings.", bold_prefix="Scientific visualisations: ")
builder.add_numbered("10.", "A comprehensive scientific report documenting the background, objectives, study area, datasets, methodology, results, discussion, conclusions, and recommendations.", bold_prefix="Technical report: ")
builder.add_paragraph(
    "All figures, tables, and maps must have appropriate titles, captions, legends, units, and data sources. "
    "Results should be interpreted scientifically rather than presented as images or numerical outputs without explanation."
)

builder.add_spacer(6)

# SECTION 3
builder.add_h1("3. GITHUB REPOSITORY AND SUBMISSION REQUIREMENTS")
builder.add_paragraph("All assignment work must be submitted through GitHub. Email submissions will not be accepted.", bold_prefix="Submission Policy: ")
builder.add_paragraph("Each student must fulfill the following technical submission criteria:")
builder.add_numbered("1.", "Create an individual GitHub repository dedicated to Practical Assignment 1.")
builder.add_numbered("2.", "Use a clear repository name, preferably AGE418_Practical_Assignment_1.")
builder.add_numbered("3.", "Upload all Google Earth Engine scripts, processing scripts, technical documentation, relevant figures, maps, tables, and the final report in PDF format.")
builder.add_numbered("4.", "Include a README.md file containing: Student full name & registration number; Assignment title & course code; Study area & objectives; Datasets & sources; Description of repository folders and files; Step-by-step instructions for reproducing the analysis.")
builder.add_numbered("5.", "Ensure that the repository contains the final and complete version of the assignment before submission.")
builder.add_numbered("6.", "Make the repository public so the instructor can access and review it. Alternatively, if using a private repository, invite the instructor as a collaborator using the GitHub username kadefue.")
builder.add_numbered("7.", "Submit the repository URL through the instructor's designated GitHub submission channel, as communicated during the course.")

builder.add_callout(
    "Mandatory Submission Protocol & Instructor Handle:",
    "Important: Merely mentioning @kadefue in a README or sharing a GitHub username does not constitute repository submission. The actual repository URL must be provided, and the instructor must have access to its contents.\nOfficial Instructor GitHub Handle: @kadefue | Submission Deadline: 8 December 2026."
)

builder.add_spacer(6)

# SECTION 4
builder.add_h1("4. PEDAGOGICAL GUIDELINES & KEY RECOMMENDATIONS")
builder.add_callout(
    "Research-Oriented Practical Framework:",
    "This assignment is designed as a research-oriented practical exercise, not simply a collection of satellite image processing tasks. Students must demonstrate that they can acquire, process, integrate, analyse, interpret, and document multi-source remote sensing and climate data using reproducible, version-controlled workflows."
)
builder.add_paragraph("Students must pay particular attention to the following three critical instructions:")
builder.add_numbered("1.", "Students should establish the actual seasonal rainfall and cropping calendar for Kondoa and Bahi through empirical CHIRPS/ERA5 data and local literature. In central Tanzania (semi-arid Dodoma), rainfall is predominantly unimodal (Msimu, Dec–April). Students must explicitly address whether the classic bimodal Masika/Vuli framework applies, and explain local seasonal definitions rather than forcing unverified assumptions.", bold_prefix="Do Not Force Masika and Vuli Assumptions: ")
builder.add_numbered("2.", "The 23 vegetation indices listed in Section 1.3 are candidates. Students are required to select, compute, and evaluate at least eight (8) optical indices and relevant Sentinel-1 dual-polarization radar indicators. The quality of index selection, physical justification, sensitivity comparison, and agricultural interpretation is far more important than the absolute number calculated.", bold_prefix="Quality over Quantity of Vegetation Indices: ")
builder.add_numbered("3.", "Public repositories are the recommended submission mode. If choosing a private repository, students must formally invite the instructor (@kadefue) as a collaborator with read access before the deadline. Simply sharing a username or referencing @kadefue in markdown is not a valid submission.", bold_prefix="Verifiable GitHub Submission Protocol: ")

builder.add_spacer(6)

# SECTION 5
builder.add_h1("5. GENERAL ASSESSMENT CRITERIA")
builder.add_paragraph("The assignment will be assessed based on:")
builder.add_bullet("Correct acquisition and preprocessing of satellite and climate datasets.")
builder.add_bullet("Appropriate application of remote sensing and vegetation index techniques.")
builder.add_bullet("Integration of Sentinel-1 and Sentinel-2 observations.")
builder.add_bullet("Quality of rainfall and temperature analysis.")
builder.add_bullet("Scientific validity of the analytical methods.")
builder.add_bullet("Quality of spatial and temporal visualisations.")
builder.add_bullet("Interpretation of findings and relevance to precision agriculture.")
builder.add_bullet("Reproducibility, code organisation, and technical documentation.")
builder.add_bullet("Overall quality of the scientific report.")

builder.add_spacer(3)
builder.add_paragraph(
    "Students are expected to demonstrate their own understanding of the methods, justify their analytical choices, "
    "and produce reproducible results.",
    bold_prefix="Academic Expectation: ",
    italic=True
)

# Output destinations
pdf_bytes = builder.build_pdf_bytes()

destinations = [
    os.path.join(base_dir, "AGE 418", "Assignment 2026-2027", "Assignment 1.pdf"),
    os.path.join(base_dir, "AGE 418", "Assignment 2026", "2027", "Assignment 1.pdf")
]

for dst in destinations:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as f:
        f.write(pdf_bytes)
    print(f"[Success] Generated {dst} ({len(pdf_bytes)} bytes, {len(builder.pages)} pages)")
