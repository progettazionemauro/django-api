+++
title = 'Il_mio_primo_post'
date = 2024-03-18T10:30:18+01:00
draft = true
ShowToc= true
tags = ["adventure", "foodie", "travel", "cooking", "music", "photography", "fitness", "nature", "fun", "inspiration"]
categories = ["adventure", "food", "technology", "sports", "fashion", "health", "art", "entertainment", "science", "lifestyle"]
[cover]
    image= "img/download.png"
    alt="Questa è un'immagine!"
    caption="Questo è il titolo"

+++

**Installazione di un tema ed attivazione del sito**

Si fa riferimento al Papermod Theme

In ubuntu istallare (This command will install the Go programming language using Snap with classic confinement)

`sudo snap install go --class`

Create a new Hugo site

```
hugo new site MyFreshWebsite --format yaml
# replace MyFreshWebsite with name of your website
```

Clonare il tema come modulo Hugo:

git clone https://github.com/adityatelange/hugo-PaperMod themes/PaperMod --depth=1

### Finally set theme as PaperMod in your site config

In `config.yml` add:

```
theme: ["PaperMod"]
```

After: 

1. **Verify Module Initialization:** After running `hugo mod init github.com/progettazionemauro/toha`, ensure that a `go.mod` file is created in the root directory of your Hugo project.
2. **Check Module Configuration:** Open the `go.mod` file and verify that the module reference for your theme (`github.com/progettazionemauro/toha`) is listed.
3. **Start Hugo Server:** Run `hugo server` to start the Hugo development server.
4. **View Your Site:** Visit the URL displayed in your terminal to view your site. The theme should automatically be picked up by Hugo since it's imported as a module.
5. **Customization:** If the theme provides customization options or parameters, you may need to refer to the theme's documentation or source code to understand how to customize it. Depending on how the theme is designed, you may be able to configure it using Hugo parameters or by modifying template files.

Since you're using Hugo Modules, you typically don't need to manually specify the theme in your configuration file. Hugo will automatically detect and use the theme module specified in the `go.mod` file.

If you encounter any issues or need specific customization guidance for the theme, it's often helpful to refer to the theme's documentation or reach out to the theme author for assistance.
