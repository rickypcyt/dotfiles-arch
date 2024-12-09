-- bootstrap lazy.nvim, LazyVim and your plugins
require("config.lazy")
-- En tu archivo de configuración de Neovim, por ejemplo init.lua
require("lazy").setup({
    {
        "tiagovla/tokyodark.nvim",
        opts = {
            -- opciones personalizadas si las necesitas
        },
        config = function(_, opts)
            require("tokyodark").setup(opts)  -- Llama a la configuración del tema
            vim.cmd [[colorscheme tokyodark]]  -- Activa el tema
        end,
    },
    -- Puedes agregar más plugins aquí
})
