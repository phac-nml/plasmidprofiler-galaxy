# Usage

PlasmidProfiler is implemented as a set of tools and a workflow within the [Galaxy][] platform.  PlasmidProfiler can be installed within an existing Galaxy infrastructure, or provided virtual machines and [Docker][] images can be downloaded with both Galaxy and PlasmidProfiler.  Please see the [Install][] guide for more details.

## Install

The easiest way to get started is to use [Docker][].  To both install Docker and get PlasmidProfiler, please run:

```bash
curl -sSL https://get.docker.com/ | sh # Installs Docker
sudo docker run -t -p 48888:80 jencabral/plasmidprofiler_0_1_6 # Downloads and runs PlasmidProfiler and Galaxy 
```

This will install Docker, download the PlasmidProfiler Galaxy docker image, and run this image in a Docker container.  This will take a while to fully download and start up.  You may have to start the `docker` service after installation for Docker to work.  This should be a command like `sudo service docker start`, or `sudo systemctl start docker` depending on your system.  See the [Docker Install][] guide for more details.

Once running, you may log into the PlasmidProfiler Galaxy instance by going to <http://localhost:48888> on your machine.  This should present you with a screen like the following:

![plasmidprofiler-galaxy-docker][]

Once Galaxy is started, please login (**User > Login**) with the credentials `admin@galaxy.org` and `admin`.

**Note: By default, Docker will not persist any data after it is shutdown.  To permanently save information run through PlasmidProfiler/Galaxy with Docker, please see the [PlasmidProfiler Docker] guide.**

# Input Data

PlasmidProfiler pipeline takes as input a set of sequence reads, and the included plasmid databases.  A very basic dataset can be found at [test-data.tar.gz][].

The data must first be uploaded to the PlasmidProfiler Galaxy instance before it can be used.  This can be accomplished by navigating to **Get Data > Upload File** in your web browser.

![get-data-galaxy][]

This should bring up a window for uploading files to Galaxy.

![get-data-window-galaxy][]

*Note: when selecting the **fastq** files, please make sure the data type is set to **fastqsanger**.  See [Preparing Sequence Reads](#preparing-sequence-reads).*

## Plasmid Databases

The included plasmid databases need to be imported into your current history. This can be accomplished by navigating to **Shared Data > Data Libraries** in your web browser. 

![shared-data-libraries][]

Click on the Plasmid Profiler library. Select the Databases folder and then press "Import to History"

![import-to-history][]


## Sequence Reads

Sequence reads should be uploaded to Galaxy in the **fastqsanger** format.  From the upload window, select the all the sequence reads under `reads/` and set the type to **fastqsanger** (Galaxy defaults to type **fastq**, which is not as useful).  This should look like the following.

![upload-sequence-reads][]

When all the reads are uploaded, you should see the following in your Galaxy history.

![upload-sequence-reads-history][]

## Preparing Sequence Reads

SNVPhyl makes use of a data structure in Galaxy called [Dataset Collections][].  Dataset collections allow the grouping of files into a single entry in Galaxy to execute in a workflow.  The SNVPhyl workflow assumes all sequence reads are combined in a paired-end dataset collection, which will properly associated each pair of sequence reads files.

To construct a paired dataset collection of reads in Galaxy, please do the following:

1.  Select the **Operate on multiple datasets** button in the Galaxy histories panel.

    ![operate-multiple-datasets][]

2.  Select all the **fastq** sequence files.

    ![select-sequence-files][]

3.  Select **For all selected > Build List of Dataset Pairs**

    ![build-list-pairs][]

4.  In the screen that follows, all the sequence reads should be automatically paired.

    ![paired-data-screen1][]

    Give the collection of files a name and select **Create list**.

    ![paired-data-screen2][]

    The set of paired files should appear in your Galaxy history.

    ![paired-data-list][]

# Running the Workflow

Once all the data has been prepared, the workflow can be run.  The installed workflows can be found in the Galaxy **Tools** panel at the left of the screen.

![tools-panel][]

Near the bottom.

![installed-workflows][] 

Or, alternatively, by clicking on the **Workflows** menu at the top ![workflow-top-menu][].

![workflows-list][]

## Parameters

All parameters for each tool can be overridden in Galaxy, but a few key parameters will appear at the top of the parameters page.

![parameters-list][]

These parameters represent:

1. **plot_title**:  This will be the title of the resulting plots.

Once parameters are selected, the input files can be selected.

## Input files

Galaxy should automatically detect the appropriate input files from the current history for the Paired End Fastqs and the Plasmid Database, however you will need to select the correct file for the Plasmidfinder + APC database. Please verify that it has picked up the correct files.

![input-files-selection][]

## Run

START FROM HERE NEXT TIME

Once the parameters and input files have been selected, you can run the workflow by clicking the **Run workflow** at the bottom of the screen.

![run-workflow][]

This will start the workflow.  You may have to refresh your page to see each step being executed.  This should look like:

![workflow-running][]

# Results

On completion each item in the Galaxy history should show up as green.  The very top should contain the main output files.

![output-files][]

In particular, the file **phylogeneticTree.newick** contains the ouput phylgeny.  This can be quickly visualied using the built-in viewer in Galaxy by selecting **Visuzlize in Phyloviz**.

![phylogeny-vis][]

This loads up the phylogeny in a viewer similar to below.

![example-phylogeny][]

All intermediate files in the workflow can be inspected by first selecting the Galaxy history options.

![history-options][]

Then selecting **Unhide hidden datasets**.

![unhide-hidden-datasets][]

For more information about interacting with data from Galaxy, please see the [Learn Galaxy][] page.

# Managing Errors

When an error occurs for a tool in Galaxy, the dataset boxes in the history will show up in red.  Clicking on the **bug** icon will bring up more details about an error.

![galaxy-dataset-error][]

![galaxy-dataset-error-details][]

In this case, the message reports no valid phylip alignment.  Checking the [SNV/SNP Alignment][] file shows it is empty.

![snp-alignment-error][]

This indicates no valid SNVs were detected, which could be caused by very little data in one more more samples.  Confirming this can be done by examining some of the additional output files decribed in the [Output][] section.

If examining the datasets does not help diagnose the issue, then examining the Galaxy log files can be helpful.  With Docker, these should be printed to the screen.  With other installation methods the location may vary.  Please refer to the [Install][] section for more details.

# Output Manipulation in R

See the [Example Section][] for details on how to use the other package functions in an R environment. 

[Galaxy]: http://galaxyproject.org/
[Docker]: https://www.docker.com/
[Docker Install]: https://docs.docker.com/installation/
[Install]: ../install/
[plasmidprofiler-galaxy-docker]: images/plasmidprofiler-galaxy-docker.png
[test-data.tar.gz]: ../workflows/SNVPhyl/test-data.tar.gz
[get-data-galaxy]: images/get-data-galaxy.png
[get-data-window-galaxy]: images/get-data-window-galaxy.png
[upload-sequence-reads]: images/upload-sequence-reads.png
[upload-reference]: images/upload-reference.png
[shared-data-libraries]: images/shared-data-libraries.png
[import-to-history]: images/import-to-history.png
[upload-invalid-positions]: images/upload-invalid-positions.png
[upload-sequence-reads-history]: images/upload-sequence-reads-history.png
[BED]: http://genome.ucsc.edu/FAQ/FAQformat#format1
[operate-multiple-datasets]: images/operate-multiple-datasets.png
[select-sequence-files]: images/select-sequence-files.png
[build-list-pairs]: images/build-list-pairs.png
[paired-data-screen1]: images/paired-data-screen1.png
[paired-data-screen2]: images/paired-data-screen2.png
[paired-data-list]: images/paired-data-list.png
[installed-workflows]: images/installed-workflows.png
[parameters-list]: images/parameters-list.png
[input-files-selection]: images/input-files-selection.png
[run-workflow]: images/run-workflow.png
[workflow-running]: images/workflow-running.png
[output-files]: images/output-files.png
[phylogeny-vis]: images/phylogeny-vis.png
[example-phylogeny]: images/example-phylogeny.png
[history-options]: images/history-options.png
[unhide-hidden-datasets]: images/unhide-hidden-datasets.png
[Learn Galaxy]: https://wiki.galaxyproject.org/Learn
[Examples]: examples/
[tools-panel]: images/tools-panel.png
[PlasmidProfiler Docker]: ../install/docker.md
[Dataset Collections]: https://wiki.galaxyproject.org/Documents/Presentations/GCC2014?action=AttachFile&do=get&target=Chilton.pdf
[galaxy-dataset-error]: images/galaxy-dataset-error.png
[galaxy-dataset-error-details]: images/galaxy-dataset-error-details.png
[snp-alignment-error]: images/snp-alignment-error.png
[SNV/SNP Alignment]: output.md#snvsnp-alignment
[Output]: output.md
[workflows-list]: images/workflows-list.png
[workflow-top-menu]: images/workflow-top-menu.png
[Example Section]: ../examples/example-run.md
