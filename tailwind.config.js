/** @type {import('tailwindcss').Config} */

const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./solutions/**/*.{html,js}",
    "./**/*.{html,js}"
  ],
  theme: {
    fontFamily: {
        sans: ['"DM Sans"', ...defaultTheme.fontFamily.sans]
    },
    extend: {},
  },
  plugins: [],
}

