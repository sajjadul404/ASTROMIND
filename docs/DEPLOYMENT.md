# Local preview, new GitHub repository and GitHub Pages

## 1. Preview locally

Open the extracted folder in VS Code. In the VS Code PowerShell terminal:

```powershell
py -m http.server 8000
```

Or if `python` is available:

```powershell
python -m http.server 8000
```

Visit `http://localhost:8000`. No frameworks, package installation or API keys are required.

## 2. Validate repository files

```powershell
python scripts/validate_repo.py
```

Or on Windows:

```powershell
py scripts/validate_repo.py
```

## 3. Create a brand-new repository under your username

Recommended: [GitHub CLI](https://cli.github.com/) installed and authenticated. Run `gh auth login` once if needed.

From **inside this project folder**:

```powershell
git init -b main
git add -A
git commit -m "Launch ASTROMIND Figma project showcase"
gh repo create AstroMind-Orbit-Smiths-2026 --public --source=. --remote=origin --push
```

`gh repo create` creates a new repository under whichever GitHub account is authenticated. If the name already exists, choose a different unused name. **Do not run `git push --force`** or upload this package on top of the team's repo unless you explicitly want to change it.

The included `PUSH_NEW_REPOSITORY.ps1` can do these steps after confirming that `gh` and `git` are installed and you are logged in.

## 4. Enable GitHub Pages

In your new repository:

1. Open **Settings → Pages**.
2. Under **Build and deployment**, choose **Deploy from a branch**.
3. Choose branch **`main`** and folder **`/ (root)`**, then **Save**.
4. Use the URL GitHub shows for your new Pages site.

The website uses relative links so it works under a project-style GitHub Pages URL. The `.nojekyll` file is included because no Jekyll build is needed.

## 5. Make the Figma prototype public to viewers

Use Figma's sharing/presentation options to make the prototype viewable to anyone with the link as intended. Test the link in a private browser window. The repository cannot publish the editable Figma source file unless you export and add it yourself.

## Pre-push checklist

- [ ] Original images present under `assets/images/` and visible in README preview
- [ ] Figma prototype link opens without requiring team-only access
- [ ] Team names verified against script and poster
- [ ] README does not imply unimplemented NASA APIs are integrated
- [ ] Permission obtained to publish team photos/poster and original design
- [ ] Uploaded presentation PDF is the intended version
- [ ] `python scripts/validate_repo.py` passes
- [ ] `git status` is clean after pushing

## Updating later

```powershell
git add -A
git commit -m "Update ASTROMIND project showcase"
git push
```
