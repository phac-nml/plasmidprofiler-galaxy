# Plasmid Profiler Pipeline: Heatmap Display of Plasmid Content in WGS Data

Plasmid profiler is a pipeline to perform comparative plasmid content analysis. It is designed to rapidly bin plasmid content using KAT, Short Read Sequence Typing, and BLAST followed by scoring hits based on a combined measure of maximized coverage and minimized sequence divergence. Hits are then visualized in both static and interactive heatmaps as well as arranged as tabular results. [Input][] is provided in the form of a collection of whole genome sequence reads along with a reference plasmid database and replicon/gene of interest database.  The [output][] from the pipeline consists of a png heatmap, an interactive html heatmap, and tabular format results of all plasmids identified and their respective scores.

[![exampleHM][]][exampleHM]

# Operation

The stages of the Plasmid Profiler pipeline are as follows:

[![PP-flowchart][]][PP-flowchart]

1. Preparing input files including:  
    1. A set of sequence reads.  
    2. A reference plasmid database.  
    3. Plasmid Finder replicon database along with genes of interest.  
2. [KAT][] identifies database plasmids represented in the reads and creates an individualized plasmid database per isolate.
3. [SRST2][] identifies plasmid hits from the individual per isolate databases.
4. [BLAST][] identifies the incompatibility groups and genes of interest on hit plasmids.
5. Parse and score the identified plasmids using the [PlasmidProfiler][] R package.
6. Produce visualizations and export tables using the [PlasmidProfiler][] R package.

Plasmid Profiler is implemented as a [Galaxy][] workflow, with each of these stages implemented using a specific Galaxy tool.

[![plasmid-profiler-overview-galaxy][]][plasmid-profiler-overview-galaxy]

More information on the operation and installation of the pipeline can be found in the [Usage][] and [Installation][] sections.

# Contact

Comments, questions, or issues can be sent to:  
Adrian Zetner <adrian.zetner@canada.ca>   
Jennifer Cabral <jennifer.cabral@canada.ca>

<!-- Links in order of sight in the page -->
[exampleHM]: images/exampleheatmap.png
[KAT]: https://github.com/TGAC/KAT
[SRST2]: https://katholt.github.io/srst2/
[BLAST]: https://blast.ncbi.nlm.nih.gov/Blast.cgi
[PlasmidProfiler]: https://cran.r-project.org/package=Plasmidprofiler


[Galaxy]: http://galaxyproject.org/
[Installation]: install/index.md
[Overview]: galaxy/index.md



[PhyML]: http://www.atgc-montpellier.fr/phyml/
[Usage]: galaxy/usage.md
[PP-flowchart]: images/PP-flowchart.png
[plasmid-profiler-overview-galaxy]: images/screenshot136.png

[output]: galaxy/output.md
[Input]: galaxy/input.md
