import { defineConfig } from "eslint/config";
import js from "@eslint/js";
import vue from "eslint-plugin-vue";
import typescript from "@typescript-eslint/eslint-plugin";
import typescriptParser from "@typescript-eslint/parser";

export default defineConfig([
    // Vue文件配置
    {
        files: ["**/*.vue"],
        plugins: {
            vue,
        },
        languageOptions: {
            parser: vue.parserServices,
        },
        rules: {
            ...vue.configs.recommended.rules,
        },
    },
    // TypeScript文件配置
    {
        files: ["**/*.ts", "**/*.tsx"],
        plugins: {
            "@typescript-eslint": typescript,
        },
        languageOptions: {
            parser: typescriptParser,
            parserOptions: {
                ecmaVersion: "latest",
                sourceType: "module",
            },
        },
        rules: {
            ...typescript.configs.recommended.rules,
        },
    },
    // JavaScript文件配置
    {
        files: ["**/*.js", "**/*.jsx", "**/*.mjs", "**/*.cjs"],
        plugins: {
            js,
        },
        rules: {
            ...js.configs.recommended.rules,
        },
    },
]); 