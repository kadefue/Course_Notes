<div align="center">

<img src="../../SUA.png" alt="Sokoine University of Agriculture Logo" width="110"/>

# SOKOINE UNIVERSITY OF AGRICULTURE
## School of Engineering and Technology (SoET)
### Department of Agricultural Engineering
**Academic Year 2026/2027**

---

# AGE 418: SENSORS AND CONTROLS FOR PRECISION AGRICULTURE
## PRACTICAL ASSIGNMENT 1

**PDF Version:** [Download Assignment 1 PDF](Assignment%201.pdf)

</div>

---

| Course Code & Title | **AGE 418: Sensors and Controls for Precision Agriculture** |
| :--- | :--- |
| **Assignment Title** | **Integrated Sentinel-1 and Sentinel-2 Remote Sensing for Assessing Seasonal Cropping Patterns, Vegetation Dynamics, and Climate–Crop Interactions in Kondoa and Bahi Districts, Dodoma Region, Tanzania (2016–2026)** |
| **Study Area** | **Kondoa and Bahi Districts, Dodoma Region, Tanzania** |
| **Target Degree Programs** | **BSc in Agricultural Engineering (BSc AGE — Year 4) & BSc in Irrigation and Water Resources Engineering (BSc IWRE — Year 4)** |
| **Assignment Character** | **Research-Oriented Practical Exercise & Reproducible Scientific Workflow** |
| **Submission Deadline** | **8 December 2026** |
| **Submission Channel** | **Individual GitHub Repository (URL Submission; Invited Collaborator: `@kadefue`)** |
| **Deliverables** | **GitHub Repository + Technical Report (PDF) + GEE Scripts + Data Visualizations** |

---

## 🎯 Programmatic Context & Engineering Relevance

This practical assignment is tailored for fourth-year undergraduate engineering students enrolled in:
* **BSc in Agricultural Engineering (BSc AGE)**: Focuses on precision crop monitoring, seasonal cropping pattern mapping, crop canopy development, Sentinel-1 radar backscatter ($VV$, $VH$, $VH/VV$) sensitivity to canopy architecture and soil surface roughness, and foundational spatial analytics for Variable Rate Technology (VRT).
* **BSc in Irrigation and Water Resources Engineering (BSc IWRE)**: Focuses on agricultural climatology, empirical rainfall calendar identification (unimodal *Msimu* dynamics), CHIRPS rainfall onset/cessation and dry spell frequency, ERA5-Land temperature dynamics, vegetation water content and moisture stress indices (NDMI, MSI, NDWI), and crop water resilience in semi-arid environments.

---

## 🧭 Pedagogical Framework & Student Guidance

> [!IMPORTANT] Research-Oriented Practical Exercise
> This assignment is framed as a **rigorous research-oriented practical exercise**, not simply a collection of satellite image processing scripts. Students are expected to demonstrate the technical and critical ability to **acquire, process, integrate, analyse, interpret, and document** multi-source remote sensing (Sentinel-1 SAR, Sentinel-2 MSI) and climate datasets (CHIRPS, ERA5-Land) using fully reproducible scientific workflows.

### 🌟 Key Guidance Before Beginning

1. **Do Not Force Masika and Vuli Assumptions:**
   * Dodoma Region (including Kondoa and Bahi Districts) generally falls under a **unimodal rainfall regime (*Msimu*)**, unlike northern or coastal Tanzania which exhibit distinct bimodal (*Masika* and *Vuli*) seasons.
   * Students should **empirically establish the actual seasonal rainfall and cropping calendar** for Kondoa and Bahi using the CHIRPS rainfall and ERA5-Land data alongside local agricultural literature.
   * If a particular season is less applicable, absent, or has a distinct local definition (e.g. single long growing season vs. sporadic short rains), explicitly document, analyze, and justify this finding in your report.

2. **Index Selection: Scientific Quality Over Quantity:**
   * Students are **NOT required to compute all 23 listed indices**.
   * Requiring at least **eight (8) optical indices from Sentinel-2** and **relevant Sentinel-1 radar indicators** is scientifically defensible.
   * The **quality of index selection, sensitivity comparison, and biophysical interpretation** matters far more than the number of indices calculated. Choose indices that represent diverse physiological mechanisms: greenness, soil-background adjustment, red-edge chlorophyll, and canopy moisture.

3. **Verifiable GitHub Access & Explicit Submission Procedure:**
   * **Public repositories are the simplest and recommended option** for verification.
   * For private repositories, students **must invite the instructor (`kadefue`) as a collaborator** and verify that access is active.
   * **Merely mentioning `@kadefue` in a commit, issue, or README, or sharing a GitHub username alone, DOES NOT constitute submission.** The actual repository URL must be submitted through the course's designated submission portal.
   * **No email submissions will be accepted under any circumstances.**

---

## 1. Assignment Question

Using Google Earth Engine (GEE), Geographic Information Systems (GIS), satellite remote sensing, and climate datasets, conduct a comprehensive spatiotemporal assessment of agricultural cropping patterns, vegetation dynamics, and climate variability in Kondoa and Bahi Districts, Dodoma Region, Tanzania, covering the period 2016–2026.

The study must integrate **Sentinel-1 Synthetic Aperture Radar (SAR), Sentinel-2 Multispectral Imagery, CHIRPS rainfall data, and ERA5-Land temperature data** to investigate seasonal agricultural activities, vegetation conditions, crop development, rainfall variability, temperature dynamics, and vegetation recovery following rainfall and dry periods.

Your analysis should address the following seven (7) research components.

### 1.1 Study Area Characterisation and Mapping

1. Obtain administrative boundary data from the National Bureau of Statistics (NBS), Tanzania.
2. Extract and map Kondoa and Bahi Districts, showing their respective ward boundaries.
3. Characterise the geographical and administrative distribution of the study area.
4. Produce detailed district-level and ward-level maps with appropriate cartographic elements, including legends, scale bars, north arrows, coordinate systems, and data sources.
5. Calculate the geographical area of each district and ward where appropriate.

### 1.2 Satellite and Climate Data Acquisition and Preprocessing

Acquire, process, and analyse the following datasets using Google Earth Engine.

**A. Sentinel-1 Synthetic Aperture Radar (SAR)**

Use Sentinel-1 Ground Range Detected (GRD) imagery to:
- Extract VV and VH polarization backscatter.
- Analyse VV/VH and VH/VV backscatter ratios.
- Investigate temporal changes in radar backscatter.
- Generate appropriate radar-based vegetation indicators.
- Examine crop development, vegetation structure, and surface moisture conditions.
- Apply appropriate filtering, orbit selection, speckle reduction, and temporal compositing techniques.

**B. Sentinel-2 Multispectral Imagery**

Use Sentinel-2 Level-2A Surface Reflectance imagery to:
- Apply cloud and cloud-shadow masking.
- Extract relevant visible, red-edge, near-infrared, and shortwave-infrared bands.
- Generate monthly, seasonal, and annual satellite composites.
- Calculate vegetation indices relevant to agricultural monitoring.
- Investigate crop establishment, development, peak growth, and vegetation decline.

**C. CHIRPS Rainfall Data**

Use Climate Hazards Group InfraRed Precipitation with Station Data (CHIRPS) to:
- Estimate daily, monthly, seasonal, and annual rainfall.
- Analyse rainfall distribution and spatial variability.
- Identify rainfall onset and cessation.
- Identify dry spells and rainfall deficits.
- Investigate interannual and seasonal rainfall variability.

**D. ERA5-Land Temperature Data**

Use ERA5-Land to:
- Extract 2 m air temperature.
- Calculate monthly, seasonal, and annual temperature statistics.
- Examine mean, minimum, and maximum temperature conditions using appropriate temporal aggregations.
- Analyse seasonal and interannual temperature variability.
- Investigate potential relationships between temperature conditions and vegetation development.

*Note on Units:* Convert ERA5-Land temperature measurements from Kelvin to degrees Celsius before reporting results.

> [!NOTE] Data Coverage Notice (2016–2026)
> Use the period 2016–2026, subject to actual data availability. Clearly document the data acquisition dates and acknowledge that 2026 may represent an incomplete year at the time of analysis.

### 1.3 Vegetation Index Computation and Analysis

Calculate and analyse important vegetation indices using Sentinel-2 imagery. Consider the following candidate indices and explain their relevance to agricultural monitoring:

**A. General Vegetation Greenness and Crop Growth**
1. Normalized Difference Vegetation Index (NDVI)
2. Enhanced Vegetation Index (EVI)
3. Two-Band Enhanced Vegetation Index (EVI2)
4. Green Normalized Difference Vegetation Index (GNDVI)

**B. Soil-Adjusted Vegetation Indices**
5. Soil Adjusted Vegetation Index (SAVI)
6. Modified Soil Adjusted Vegetation Index (MSAVI2)
7. Optimized Soil Adjusted Vegetation Index (OSAVI)

**C. Chlorophyll and Crop Health Indices**
8. Normalized Difference Red Edge Index (NDRE)
9. Chlorophyll Index Red Edge (CIred-edge)
10. MERIS Terrestrial Chlorophyll Index (MTCI)

**D. Vegetation Water Content and Moisture Stress Indices**
11. Normalized Difference Moisture Index (NDMI)
12. Moisture Stress Index (MSI)
13. Normalized Difference Water Index (NDWI)
14. Modified Normalized Difference Water Index (MNDWI)

**E. Biomass, Vegetation Disturbance, and Productivity Indices**
15. Normalized Burn Ratio (NBR)
16. Normalized Burn Ratio 2 (NBR2)
17. Near-Infrared Reflectance of Vegetation (NIRv)
18. Structure Insensitive Pigment Index (SIPI)
19. Visible Atmospherically Resistant Index (VARI)

**F. Sentinel-1 Radar-Derived Vegetation Indicators**
20. Radar Vegetation Index (RVI), using an appropriate dual-polarization formulation
21. VV/VH backscatter ratio
22. VH/VV backscatter ratio
23. Temporal VV and VH backscatter change indicators

**Analysis Requirements:**
- **Calculate at least eight (8) relevant optical vegetation indices** from Sentinel-2.
- **Calculate and analyse relevant radar indicators** from Sentinel-1.
- Explain the scientific purpose and agricultural relevance of each selected index.
- Generate spatial maps and temporal profiles.
- Compare the sensitivity of selected indices to vegetation greenness, soil background, chlorophyll, biomass, and moisture conditions.
- Identify the indices that provide the most useful information for monitoring agricultural vegetation in the study area.

Ensure that the correct Sentinel-2 spectral bands are used for each index. Distinguish vegetation moisture indices from surface-water indices and explain any limitations associated with their interpretation.

### 1.4 Seasonal Cropping Patterns and Vegetation Dynamics

Investigate agricultural vegetation dynamics across the seasonal agricultural calendar, considering their local applicability to the study area.

Specifically:
- Establish and characterise the empirical cropping periods.
- Analyse vegetation development across the identified seasons.
- Compare seasonal NDVI, EVI, SAVI, and other selected vegetation indices.
- Identify the timing of vegetation emergence, peak greenness, and decline.
- Assess spatial differences in vegetation conditions across Kondoa and Bahi.
- Examine interannual changes in seasonal vegetation patterns between 2016 and 2026.
- Identify areas exhibiting consistent, variable, or contrasting seasonal vegetation behaviour.

Use both Sentinel-1 and Sentinel-2 observations to complement the seasonal assessment.

### 1.5 Rainfall and Temperature Variability Analysis

Integrate CHIRPS rainfall and ERA5-Land temperature datasets to investigate climatic conditions across the study area.

The analysis should include:
- Monthly, seasonal, and annual rainfall distribution.
- Seasonal rainfall totals and anomalies.
- Rainfall onset and cessation.
- Dry-spell duration and frequency.
- Monthly and seasonal temperature patterns.
- Annual temperature variability and anomalies.
- Spatial distribution of rainfall and temperature.
- Comparison of climatic conditions between Kondoa and Bahi.

Investigate how rainfall and temperature variability influence agricultural vegetation development and seasonal cropping patterns.

### 1.6 Vegetation Recovery, Crop Wilting, and Moisture Stress Assessment

Investigate vegetation responses to rainfall events, prolonged dry periods, and changing temperature conditions.

The analysis should:
- Estimate vegetation recovery time following rainfall events and dry periods.
- Identify periods of vegetation greenness decline.
- Investigate possible crop wilting and vegetation moisture stress using appropriate satellite indicators.
- Examine relationships between rainfall events, temperature conditions, and vegetation recovery.
- Identify spatial differences in vegetation recovery and decline.
- Compare vegetation responses using Sentinel-1 radar indicators and Sentinel-2 optical indices.
- Assess whether vegetation recovery patterns differ between major growing cycles.

Clearly distinguish satellite-derived estimates of vegetation stress and recovery from direct field measurements of crop wilting.

### 1.7 Integrated Climate–Vegetation and Precision Agriculture Assessment

Integrate Sentinel-1, Sentinel-2, CHIRPS, and ERA5-Land datasets to investigate the relationships between climatic conditions and agricultural vegetation dynamics.

Specifically:
- Examine relationships between rainfall, temperature, and vegetation indices.
- Investigate the response of vegetation indicators to rainfall variability.
- Analyse possible temperature-related vegetation stress.
- Compare radar and optical indicators of vegetation conditions.
- Identify areas with contrasting vegetation development and recovery patterns.
- Determine which satellite and climate indicators are most informative for agricultural monitoring.
- Discuss how the findings could support precision agriculture, agricultural decision-making, and climate-informed crop management in Kondoa and Bahi.

Use appropriate statistical techniques, temporal analysis, correlation analysis, and spatial analysis to support your findings. Where appropriate, apply regression or other suitable analytical methods, ensuring that the methodology accounts for temporal dependence and avoids unsupported causal interpretations.

---

## 2. Expected Outputs and Deliverables

Students are expected to produce the following ten (10) deliverables:

1. **Study area maps:** District and ward-level administrative maps of Kondoa and Bahi.
2. **Satellite data products:** Processed Sentinel-1 and Sentinel-2 datasets.
3. **Vegetation index products:** Spatial maps and temporal profiles of at least eight optical vegetation indices and relevant radar-derived indicators.
4. **Seasonal analysis:** Comparative assessment of vegetation dynamics across the empirical growing seasons.
5. **Rainfall analysis:** CHIRPS-derived rainfall maps, seasonal totals, anomalies, and temporal trends.
6. **Temperature analysis:** ERA5-Land-derived temperature maps, seasonal patterns, and temporal trends.
7. **Vegetation recovery assessment:** Analysis of vegetation recovery, decline, and potential moisture stress.
8. **Integrated analysis:** Statistical and spatial investigation of climate–vegetation relationships.
9. **Scientific visualisations:** At least 10 high-quality figures, tables, and maps collectively presenting the major findings.
10. **Technical report:** A comprehensive scientific report documenting the background, objectives, study area, datasets, methodology, results, discussion, conclusions, and recommendations.

All figures, tables, and maps must have appropriate titles, captions, legends, units, and data sources. Results should be interpreted scientifically rather than presented as images or numerical outputs without explanation.

---

## 3. GitHub Repository and Submission Requirements

> [!IMPORTANT] Submission Procedure
> **All assignment work must be submitted through GitHub. Email submissions will not be accepted under any circumstances.**

Each student must:

1. **Create an individual GitHub repository** dedicated to Practical Assignment 1.
2. Use a clear repository name, preferably `AGE418_Practical_Assignment_1`.
3. Upload all Google Earth Engine scripts, processing scripts, technical documentation, relevant figures, maps, tables, and the final report in PDF format.
4. Include a comprehensive `README.md` file containing:
   - Student's full name and registration number.
   - Assignment title and course code.
   - Study area and research objectives.
   - Datasets and their sources.
   - Description of repository folders and files.
   - Clear, step-by-step instructions for reproducing the analysis.
5. Ensure that the repository contains the final and complete version of the assignment before submission.
6. **Repository Visibility & Access:**
   - **Public Repository (Recommended):** Simplest option for immediate instructor verification.
   - **Private Repository:** You **must invite the instructor as a collaborator** using the GitHub username **`kadefue`**.
7. **Submit the Repository URL:** Submit the direct repository URL through the instructor's designated submission channel as communicated in class.

> [!WARNING] Verifiable Submission Mandate
> Merely mentioning `@kadefue` in a README, commit message, or issue, or sharing a GitHub username alone, **DOES NOT constitute repository submission**. The actual, active repository URL must be provided, and the instructor must have verifiable read access to its contents.

* **Official Instructor GitHub Handle:** `@kadefue`
* **Submission Deadline:** **8 December 2026**

---

## 4. General Assessment Expectations

The assignment will be assessed based on:

- **Data Acquisition & Preprocessing:** Correct acquisition, filtering, and cloud/speckle masking of satellite and climate datasets.
- **Remote Sensing Methodology:** Sound application of vegetation indices and radar formulations.
- **Sensor Fusion:** Insightful integration of Sentinel-1 radar and Sentinel-2 optical observations.
- **Climate Analysis:** Quality of rainfall and temperature variability and anomaly analysis.
- **Scientific Validity:** Rigor of spatial, temporal, and statistical analytical methods.
- **Visual Presentation:** Cartographic and visual excellence of maps, charts, and temporal profiles.
- **Precision Agriculture Relevance:** Depth of interpretation and practical relevance of findings to smallholder precision agriculture and climate adaptation.
- **Reproducibility & Organization:** Clean code organization, technical documentation, and workflow reproducibility.
- **Overall Scientific Quality:** Clarity, depth, and rigor of the final written technical report.

> [!TIP] Pedagogical Philosophy
> The resulting assignment is suitable for an advanced practical engineering course because it requires students to combine **remote sensing, climate data, spatial analysis, time-series analysis, and reproducible scientific programming**. Students are expected to demonstrate their own understanding of the methods, justify their analytical choices, and produce reproducible results.
