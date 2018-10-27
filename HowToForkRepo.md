## Fork our final project Git Hub repository

A *fork* is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

##### Propose changes to someone else's project

A great example of using forks to propose changes is for bug fixes. Rather than logging an issue for a bug you've found, you can:

- Fork the repository.
- Make the fix.
- Submit a *pull request* to the project owner.

If the project owner likes your work, they might pull your fix into the original repository!

##### Use someone else's project as a starting point for your own idea.

At [the heart of open source](http://opensource.org/about) is the idea that by sharing code, we can make better, more reliable software.

When creating your public repository from a fork of someone's project, make sure to include a [license file](http://choosealicense.com/) that determines how you want your project to be shared with others.

For more information on open source, specifically how to create and grow an open source project, we've created [Open Source Guides](https://opensource.guide/) that will help you foster a healthy open source community by recommending best practices for creating and maintaining repositories for your open source project. You can also take a free [GitHub Learning Lab](https://lab.github.com/) course on maintaining open source communities.

#### Step 1: Fork the repo

Forking a repository is a simple two-step process. We've created a repository for you to practice with!

1. On GitHub, navigate to the https://github.com/webbshasta/pfb2018_FinalProject trepository.
2. In the top-right corner of the page, click the button **Fork**.

#### Step 2: Create a local clone of your fork

Right now, you have a fork of the pfb2018_FinalProject repository, but you don't have the files in that repository on your computer. Let's create a *clone* of your fork locally on your computer.

1. On GitHub, navigate to **your fork** of the pfb2018_FinalProject repository.

2. ![Clone or download button](https://help.github.com/assets/images/help/repository/clone-repo-clone-url-button.png)Under the repository name, click **Clone or download**.

3. ![Clone URL button](https://help.github.com/assets/images/help/repository/https-url-clone.png)In the Clone with HTTPs section, click  to copy the clone URL for the repository.

4. Open Terminal.

5. Type `git clone`, and then paste the URL you copied in Step 2. It will look like this, with your GitHub username instead of `YOUR-USERNAME`:

   ```
   git clone https://github.com/YOUR-USERNAME/pfb2018_FinalProject
   ```

6. Press **Enter**. Your local clone will be created.

   ```
   git clone https://github.com/YOUR-USERNAME/pfb2018_FinalProject
   Cloning into `pfb2018_FinalProject`...
   remote: Counting objects: 10, done.
   remote: Compressing objects: 100% (8/8), done.
   remove: Total 10 (delta 1), reused 10 (delta 1)
   Unpacking objects: 100% (10/10), done.
   ```

Now, you have a local copy of your fork of the pfb2018_FinalProject repository!

#### Step 3: Configure Git to sync your fork with the original pfb2018_FinalProject repository

When you fork a project in order to propose changes to the original repository, you can configure Git to pull changes from the original, or *upstream*, repository into the local clone of your fork.

1. On GitHub, navigate to the webbshasta/pfb2018_FinalProject repository.

2. ![Clone or download button](https://help.github.com/assets/images/help/repository/clone-repo-clone-url-button.png)Under the repository name, click **Clone or download**.

3. ![Clone URL button](https://help.github.com/assets/images/help/repository/https-url-clone.png)In the Clone with HTTPs section, click  to copy the clone URL for the repository.

4. Open Terminal.

5. Change directories to the location of the fork you cloned in [Step 2: Create a local clone of your fork](https://help.github.com/articles/fork-a-repo/#step-2-create-a-local-clone-of-your-fork).

   - To go to your home directory, type just `cd` with no other text.
   - To list the files and folders in your current directory, type `ls`.
   - To go into one of your listed directories, type `cd your_listed_directory`.
   - To go up one directory, type `cd ..`.

6. Type `git remote -v` and press **Enter**. You'll see the current configured remote repository for your fork.

   ```
   git remote -v
   origin  https://github.com/YOUR_USERNAME/pfb2018_FinalProject.git (fetch)
   origin  https://github.com/YOUR_USERNAME/pfb2018_FinalProject.git (push)
   ```

7. Type `git remote add upstream`, and then paste the URL you copied in Step 2 and press **Enter**. It will look like this:

   ```
   git remote add upstream https://github.com/webbshasta/pfb2018_FinalProject
   ```

8. To verify the new upstream repository you've specified for your fork, type `git remote -v`again. You should see the URL for your fork as `origin`, and the URL for the original repository as `upstream`.

   ```
   git remote -v
   origin    https://github.com/YOUR_USERNAME/pfb2018_FinalProject.git (fetch)
   origin    https://github.com/YOUR_USERNAME/pfb2018_FinalProject.git (push)
   upstream  https://github.com/webbshasta/pfb2018_FinalProject (fetch)
   upstream  https://github.com/webbshasta/pfb2018_FinalProject (push)
   ```

Now, you can keep your fork synced with the upstream repository with a few Git commands. 

