module.exports = {
    root: true,
    env: {
        node: true
    },
    extends: [
        'plugin:vue/essential',
        '@vue/standard'
    ],
    parserOptions: {
        parser: 'babel-eslint'
    },
    rules: {
        'no-console': 'off',
        'no-debugger': 'off',
        'no-tabs': 'off',
        'no-mixed-spaces-and-tabs': 'off',
        'no-useless-escape': 'off',
        'no-prototype-builtins': 'off',
        'no-useless-return': 'off',
        'import/first': 'off',
        'camelcase': 'off',
        'dot-notation': 'off',
        'one-var': 'off',
        'space-before-function-paren': 'off',
        'multi-word-component-names': 'off',
        'no-trailing-spaces': 'off',
        'comma-dangle': 'off',
        'quotes': 'off',
        'semi': 'off'
    }
}