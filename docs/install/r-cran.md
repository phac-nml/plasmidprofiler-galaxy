R - CRAN Library
==========

A [VirtualBox][] virtual machine is provided for running SNVPhyl along with Galaxy.  This machine requires at least **4 GB** of memory and **4 CPUs** to properly run.  The machine can be quickly launched using [Vagrant][] with the following commands.

```bash
git clone https://irida.corefacility.ca/analysis-pipelines/snvphyl-galaxy
cd snvphyl-galaxy/vagrant
vagrant up
```

Running `vagrant up` will download and launch the virtual machine.  Galaxy can be accessed by navigating to <http://localhost:48888>.  The default username and passwords are:

* **User:** *admin@localhost.localdomain*
* **Password:** *adminpassword*

Once logged in, the workflows for SNVPhyl can be accessed by clicking on **Workflow** at the top.

Accessing the R Library
-----------------------------


[RStudio]: https://www.virtualbox.org/
[Vagrant]:  https://www.vagrantup.com/
[Packer]: https://packer.io/
