module.exports = {
    // Automatically clear mock calls and instances between every test
    clearMocks: true,
    // An array of glob patterns indicating a set of files for which coverage information should be collected
    collectCoverageFrom: [
        './__tests__/**/*.{js,jsx}',

    ],
    // The directory where Jest should output its coverage files
    coverageDirectory: 'coverage',
    coveragePathIgnorePatterns: [ '/node_modules/', '.jest/enzyme.js', 'commitlint.config.js', 'next.config.js' ],
    // The maximum amount of workers used to run your tests.
    maxWorkers: '80%',
    moduleFileExtensions: [ 'js', 'json', 'scss', 'css' ],

    moduleNameMapper: {
        '^utils(.*)$': '<rootDir>/src/utils$1',
        '^modules(.*)$': '<rootDir>/src/modules$1',
        '^components(.*)$': '<rootDir>/src/components$1',
        '^containers(.*)$': '<rootDir>/src/containers$1',
        '\\.(css|less|sass|scss)$': '<rootDir>/__mocks__/styleMock.js',
        '\\.(gif|ttf|eot|svg|png)$': '<rootDir>/__mocks__/fileMock.js'
    },
    setupFilesAfterEnv: [ '<rootDir>/.jest/enzyme.js' ],
    snapshotSerializers: [ 'enzyme-to-json/serializer' ],
    testEnvironment: 'jsdom',
    testMatch: [ '**/test.(js)', '**/*.test.(js)', '**/?(*.)+(spec|test).js' ],
    testPathIgnorePatterns: [ '<rootDir>/.next/', '<rootDir>/node_modules/', '/__tests__/automated/' ],
    transform: {
        '^.+\\.js$': 'babel-jest'
    },
    verbose: true
}
