// eslint.config.mjs
import js from "@eslint/js";

export default [
    js.configs.recommended,
    {
        rules: {
            "no-eval": "error" // 確保會抓到 eval 的錯誤
        }
    }
];