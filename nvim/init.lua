vim.opt.clipboard = "unnamedplus"
vim.api.nvim_set_keymap('v', '<C-S-c>', '"+y', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<C-S-v>', '"+p', { noremap = true, silent = true })
vim.api.nvim_set_keymap('n', '<C-a>', 'ggVG', { noremap = true, silent = true })


-- Opciones básicas
vim.opt.number = true            -- Números de línea
vim.opt.relativenumber = true    -- Números relativos (para moverte rápido)
vim.opt.cursorline = true        -- Resalta la línea del cursor
vim.opt.expandtab = true         -- Usa espacios en lugar de tabs
vim.opt.shiftwidth = 4           -- Tamaño de indentación
vim.opt.tabstop = 4              -- Tamaño de un tab
vim.opt.smartindent = true       -- Indentación inteligente

-- Mapas de teclas
vim.g.mapleader = " "            -- Espacio como tecla líder
vim.keymap.set("n", "<leader>w", ":w<CR>", { silent = true })  -- Guardar rápido
vim.keymap.set("n", "<leader>q", ":q<CR>", { silent = true })  -- Salir rápido

-- Lazy.nvim setup
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
    vim.fn.system({
        "git",
        "clone",
        "--filter=blob:none",
        "https://github.com/folke/lazy.nvim.git",
        "--branch=stable", -- Versión estable
        lazypath,
    })
end
vim.opt.rtp:prepend(lazypath)

require("lazy").setup({
    -- Resaltado de sintaxis avanzado
    {
        "nvim-treesitter/nvim-treesitter",
        build = ":TSUpdate",
        config = function()
            require("nvim-treesitter.configs").setup({
                ensure_installed = "all", -- Instala todos los lenguajes soportados
                highlight = { enable = true },
            })
        end,
    },
    -- Fuzzy Finder
    {
        "nvim-telescope/telescope.nvim",
        dependencies = { "nvim-lua/plenary.nvim" },
        config = function()
            require("telescope").setup()
        end,
    },
    -- Autocompletado de paréntesis, corchetes, comillas, etc.
{
    "jiangmiao/auto-pairs",
    config = function()
        -- Configuración opcional, puedes dejarla vacía si no necesitas ajustes adicionales
    end,
},

    -- Barra de estado moderna
    {
        "nvim-lualine/lualine.nvim",
        dependencies = { "nvim-tree/nvim-web-devicons", opt = true },
        config = function()
            require("lualine").setup({ options = { theme = "tokyonight" } })
        end,
    },
    -- LSP Configuración básica
    {
        "neovim/nvim-lspconfig",
        config = function()
            require("lspconfig").tsserver.setup({}) -- Ejemplo para TypeScript/JavaScript
        end,
    },
    -- Autocompletado
    {
        "hrsh7th/nvim-cmp",
        dependencies = {
            "hrsh7th/cmp-nvim-lsp", -- Fuente para LSP
            "hrsh7th/cmp-buffer",   -- Fuente para buffer actual
            "hrsh7th/cmp-path",     -- Fuente para rutas de archivos
            "L3MON4D3/LuaSnip",     -- Snippets
        },
        config = function()
            local cmp = require("cmp")
            cmp.setup({
                snippet = {
                    expand = function(args)
                        require("luasnip").lsp_expand(args.body)
                    end,
                },
                sources = {
                    { name = "nvim_lsp" },
                    { name = "buffer" },
                    { name = "path" },
                },
                mapping = cmp.mapping.preset.insert({
                    ["<C-y>"] = cmp.mapping.confirm({ select = true }),
                    ["<C-Space>"] = cmp.mapping.complete(),
                }),
            })
        end,
    },
    -- Tema futurista
    {
        "folke/tokyonight.nvim",
        config = function()
            vim.cmd("colorscheme tokyonight")
        end,
    },
})

