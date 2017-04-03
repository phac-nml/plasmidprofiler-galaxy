# Plasmid Profiler #
--------------------


## Legal ##
-----------

 **Plasmid Profiler -  Docker & Galaxy**

 Copyright Government of Canada 2016-2017

 Plasmid Profiler Docker and Galaxy Tools written by: Jennifer Cabral, National Microbiology Laboratory, Public Health Agency of Canada

 Plasmid Profiler R Package Written by: Adrian Zetner, National Microbiology Laboratory, Public Health Agency of Canada

 Funded by the National Micriobiology Laboratory, Public Health Agency of Canada

 Licensed under the Apache License, Version 2.0 (the "License"); you may not use
 this file except in compliance with the License. You may obtain a copy of the
 License at:

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software distributed
 under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
 CONDITIONS OF ANY KIND, either express or implied. See the License for the
 specific language governing permissions and limitations under the License.

## Description ##
-----------------

Plasmid Profiler, a pipeline to perform comparative plasmid content analysis without the need for de novo assembly. The pipeline is designed to rapidly identify plasmid sequences by mapping reads to a plasmid reference sequence database. Predicted plasmid sequences are then annotated with their incompatibility group, if known. The pipeline allows users to query plasmids for genes or regions of interest and visualize results as an interactive heat map.  

Plasmid Profiler is freely available software released under the Apache 2.0 open source software license.  

Article pre-print available at: http://biorxiv.org/content/early/2017/03/28/121350

Detailed documentation can be found at http://plasmid-profiler.readthedocs.io/. 

This repository contains the customized [Galaxy][] tools for this pipeline as well as the source for the documentation.

## Documentation ##
-------------------

Current Documentation is available at [plasmid-profiler.readthedocs.io][]

Documentation is written using [Markdown][] and can be compiled using [mkdocs][].  To install [mkdocs][] please run:

```bash
pip install mkdocs
```

To quickly generate a site for the documentation please run:

```bash
mkdocs serve
```

This will build a site under http://localhost:8000.

[plasmid-profiler.readthedocs.io]: http://plasmid-profiler.readthedocs.io
[Markdown]: http://daringfireball.net/projects/markdown/syntax
[mkdocs]: http://www.mkdocs.org
[Galaxy]: https://galaxyproject.org/
