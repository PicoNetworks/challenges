module.exports = {
    parser: '@babel/eslint-parser',
    parserOptions: {
        ecmaVersion: 11,
    },
    env: {
        browser: true,
        node: true,
        jest: true,
    },
    globals: {
        React: 'readonly',
    },
    extends: ['airbnb', 'airbnb/hooks'],
    settings: {
        'import/resolver': {
            node: {
                paths: ['src'],
                extensions: ['.js', '.jsx', '.ts', '.tsx'],
            },
            includes: {
                paths: ['./_includes'],
            },
        },
    },
    rules: {
        'react/prop-types': 'off',
        'react/destructuring-assignment': 'off',
        'no-await-in-loop': 'off',
        'jsx-a11y/anchor-is-valid': 'off',
        'global-require': 'off',
        'import/no-dynamic-require': 'off',

        camelcase: [
            'error',
            {
                ignoreDestructuring: true,
                allow: ['access_token', 'refresh_token', 'short_code', 'plan_option_id', 'tier_id'],
            },
        ],
        indent: ['error', 4, { SwitchCase: 1 }],
        'no-param-reassign': [
            'error',
            {
                props: true,
                ignorePropertyModificationsFor: ['draftState', 'element'],
            },
        ],
        'no-underscore-dangle': [
            'error',
            {
                allow: ['_modules', '_network', '_menu', '_url', '_as', 'plan_option_id'],
            },
        ],
        'object-curly-spacing': ['error', 'always'],
        'react/jsx-filename-extension': 0,
        'react/jsx-indent': ['error', 4],
        'react/jsx-indent-props': ['error', 4],
        semi: ['error', 'never'],

        'react/jsx-props-no-spreading': 0,
        'react/no-did-update-set-state': 0,
        'react/forbid-prop-types': 0,
    },
    plugins: ['babel'],
}
