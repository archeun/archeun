module.exports = {
    purge: [],
    darkMode: false,
    theme: {
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
    plugins: [
        require('@tailwindcss/forms'),
    ],
}
