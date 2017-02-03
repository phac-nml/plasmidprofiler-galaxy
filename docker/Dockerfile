



FROM bgruening/galaxy-stable:16.07

MAINTAINER Jennifer Cabral, jen.cabral@gmail.com

ENV GALAXY_CONFIG_BRAND Plasmid Profiler v0.1.4

WORKDIR /galaxy-central

ENV GALAXY_HANDLER_NUMPROCS=3

ENV GALAXY_CONFIG_TOOL_SHEDS_CONFIG_FILE /etc/galaxy/tool_sheds_conf.xml
ADD ./galaxy/tool_sheds_conf.xml /etc/galaxy/tool_sheds_conf.xml
ADD ./galaxy/job_conf.xml /etc/galaxy/job_conf.xml

ADD ./galaxy/install_tools_modified.sh /usr/bin/install-tools-modified
RUN chmod +x /usr/bin/install-tools-modified

ADD ./galaxy/install_repository_modified.sh /usr/bin/install-repository-modified
RUN chmod +x /usr/bin/install-repository-modified

ADD ./galaxy/install_workflow_wrapper.sh /usr/bin/install-workflow
RUN chmod +x /usr/bin/install-workflow

ADD ./galaxy/plasmidprofiler-workflow-0.1.4.ga /tmp/plasmidprofiler-workflow-0.1.4.ga

ADD ./galaxy/upload_data.py /galaxy-central/scripts/api/
RUN chmod +x /galaxy-central/scripts/api/upload_data.py

# Databases
ADD ./galaxy/plasmidfinder_plusAMR.fasta /tmp/plasmidfinder_plusAMR.fasta
ADD ./galaxy/repDB3400.fasta /tmp/repDB3400.fasta

# Script to load Galaxy for install
ADD ./galaxy/startup_lite.sh /usr/bin/startup_lite
RUN chmod +x /usr/bin/startup_lite 

# Data libraries
ADD ./galaxy/setup_data_libraries.py $GALAXY_ROOT/setup_data_libraries.py
ADD ./galaxy/library_data.yaml $GALAXY_ROOT/library_data.yaml

# workaround for a Docker AUFS bug: https://github.com/docker/docker/issues/783#issuecomment-56013588
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/; rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R 0700 /etc/ssl/private; chown -R postgres /etc/ssl/private

# Turn on faster workflow scheduling
RUN sed -i -e 's/^#force_beta_workflow_scheduled_for_collections=False/force_beta_workflow_scheduled_for_collections=True/' /etc/galaxy/galaxy.ini

# Download training data and populate the data library
RUN startup_lite && \
    sleep 30 && \
    . $GALAXY_VIRTUAL_ENV/bin/activate && \
    python $GALAXY_ROOT/setup_data_libraries.py -i $GALAXY_ROOT/library_data.yaml

# Install SNVPhyl
#RUN install-repository-modified \
#    "-r 6eaba9b8bf94 --url http://galaxy-toolshed.corefacility.ca -o nml --name suite_plasmid_profiler --panel-section-id PlasmidProfiler" 

ADD plasmidprofilertools.yaml $GALAXY_ROOT/tools.yaml
RUN install-tools-modified $GALAXY_ROOT/tools.yaml
 
RUN install-workflow \
    "/tmp/plasmidprofiler-workflow-0.1.4.ga"
RUN rm /tmp/plasmidprofiler-workflow*.ga && \
    rm /tmp/plasmidfinder_plusAMR.fasta && \
    rm /tmp/repDB3400.fasta && \
    find /galaxy-central/tool_deps/ -iname '.git' | xargs -I {} rm -rf {}


# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]
