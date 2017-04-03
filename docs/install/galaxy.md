# Overview

Plasmid Profiler can be directly installed within an existing Galaxy instance.  There are a few necessary steps that must take place for installing to a local Galaxy:

1. Installing Build Dependencies
2. Installing the Plasmid Profiler dependency tools.
3. Importing the Plasmid Profiler Galaxy workflows.

## Installing Build Dependencies

Installing Galaxy tools involves building many packages from source.  Please make sure you have the standard build tools and development packages installed on the Galaxy system before proceeding.  In particular, please make sure that Perl, Python, Java, Git, Mercurial, GCC/G++, CMake, zlib-devel, ncurses-devel, expat-devel, python-pip, python-devel, libyaml-devel, and CPANminus are all installed.  

## Installing the Plasmid Profiler Tools

The Plasmid Profiler tools are managed within a Galaxy Toolshed.  In particular, within one of the `suite_plasmid_profiler` repositories at <https://toolshed.g2.bx.psu.edu/> (the [Galaxy][] Main Tool Shed).  The most recent version is `suite_plasmid_profiler`.  For more information about each version please see the [versions][] document.

![suite-plasmidprofiler-repository][]

Please select the version you wish to install and follow the steps to install this suite of tools, making sure to leave the **Handle repository dependencies?** and the **Handle tool dependencies?** options checked.

![plasmidprofiler-tool-dependencies][]

## Import Plasmid Profiler Galaxy workflows

The current Plasmid Profiler Galaxy workflow for version 0.1.6 can be found at [Plasmid Profiler 0.1.6][].  Please import these files by navigating to **Workflow > Upload or import workflow**.  On completion you should have a set of workflows available.

Installation should now be complete.  Please see the [Usage][] documentation for more information on how to use Plasmid Profiler.

[Galaxy]: https://galaxyproject.org/
[suite-plasmidprofiler-repository]: images/suite-plasmidprofiler-repository.png
[plasmidprofiler-tool-dependencies]: images/plasmidprofiler-tool-dependencies.png
[Usage]: ../galaxy/usage.md
[Plasmid Profiler 0.1.6]: ../workflows/PlasmidProfiler/0.1.6/plasmidprofiler-workflow-0.1.6.ga
[versions]: versions.md
