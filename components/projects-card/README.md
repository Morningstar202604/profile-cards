# Projects Card

A **2×2 grid** of project cards — name · description · language · stars — that
replaces the flat text list on your profile. Same starfield look as the rest of
the Profile Verse family; seven themes; live data.

## Preview

| dark | light |
|---|---|
| `THEME=dark` | `THEME=light` |

## Usage

```yaml
- name: Projects card
  uses: Morningstar202604/profile-cards/components/projects-card@v1
  with:
    user: YOUR_USERNAME
    output: assets/profile-verse/projects-card.svg

- name: Projects card (light)
  uses: Morningstar202604/profile-cards/components/projects-card@v1
  with:
    user: YOUR_USERNAME
    theme: light
    output: assets/profile-verse/projects-card-light.svg
```

## Inputs

| input | default | description |
|---|---|---|
| `user` | `Morningstar202604` | GitHub username |
| `count` | `4` | projects shown (2×2 grid; max 8) |
| `output` | `projects-card.svg` | output path |
| `token` | *(empty)* | optional; public REST data needs no token |
| `theme` | `dark` | `dark` / `light` / `rose` / `ocean` / `aurora` / `sunset` / `mint` |

## Data

Top `count` non-fork repos by stars (ties by most recent push), live from the
GitHub REST API — the card refreshes on every workflow run, so stars and the
project lineup stay current. Anonymous access works for public repos.
