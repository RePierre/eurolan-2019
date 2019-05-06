# [EuroLAN 2019](http://eurolan.info.uaic.ro/2019/index.html) #

## Prerequisites ##
- [Git for Windows](https://git-scm.com/download/win)

## Setting up the environment ##

### Installing `Docker` ###

If you have `Windows 10 Pro` or `Windows 10 Enterprise` editions installed:
- Open `Docker` download page on [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows)
- Click on the `Get Docker` button
**Note**: This step requires having a docker account.

For other versions of Windows, download [Docker Toolbox](https://docs.docker.com/toolbox/overview/).

Run the installer and follow the on-screen instructions to get `Docker` on your machine.

### Clone the repository ###
- Copy the address of this repository from the `Clone or download button`
- Open `Git GUI` application (Press `Win` button -> type `Git GUI` -> press `Enter` or type `git gui` into a command line)
- In the `Source Location` field paste the address from the first step
- In the `Target Directory` specify where you want to clone (something like `C:\Git\eurolan-2019`)
- Make sure that `Recursively clone submodules` checkbox is checked
- Press the `Clone` button

### Build the `NLP-Cube` image ###
This step will build a `Docker` image of [NLP-Cube](https://github.com/adobe/NLP-Cube) - an open source natural language processing pipeline.

To buid the image:
- Open a command prompt or PowerShell as administrator
- Navigate to the directory where the repository was cloned (e.g. `cd C:\Git\eurolan-2019`)
- Run the following command

``` powershell
docker build -t eurolan2019/nlp-cube -f .\nlp-cube\docker\Dockerfile --build-arg extranotebook=notebooks/eurolan-2019.ipynb --build-arg extranotebookname=eurolan-2019 .
```
**Note**: Make sure to include the final `.` in the command. It specifies the build context.

When the build is finished, run `docker images` in the same command window. You should see `eurolan2019/nlp-cube` in the `REPOSITORY` column of the output.
