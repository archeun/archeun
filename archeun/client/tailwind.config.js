const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    purge: [],
    darkMode: false,
    theme: {
        screens: {
            'xs': '460px',
            ...defaultTheme.screens,
        },
        extend: {
            colors: {
                archTeal: '#17B890',
                archTealDark: '#175676',
                archRed: '#F45B69',
                archYellow: '#F7CE5B',
                archGray: '#585563',
            },
        },
    },
    variants: {
        extend: {},
    },
    plugins: [],
}
