/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./**/*.html"
  ],
  theme: {
    fontFamily: {
        sans: ['"DM Sans"', ...defaultTheme.fontFamily.sans]
    },
    extend: {},
  },
  plugins: [],
}

