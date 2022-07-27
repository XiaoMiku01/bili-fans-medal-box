<h1>bili-fans-medal-box</h1>
Show your bili-fans-medals in a gihub gist

## Setup  
### Prep work
1. Create a new public GitHub Gist and copy the gist id (https://gist.github.com/)  
`https://gist.github.com/XXXX/`**`xxxxxxxxxxxxxxxx`**.

2. Create a token with the `gist` scope and copy it. (https://github.com/settings/tokens/new)  
3. Login in BiliBili (https://www.bilibili.com) and copy the `cookie` with Developer Tools (`F12`)
    
### Setup  
1. Fork this repo
2. Create `actions secrets`
    - `GH_GIST_ID`: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
    - `GH_TOKEN`: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
    - `BILI_COOKIE`: `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`  
3. Enable GitHub Actions