// rollup.config.js
import resolve from 'rollup-plugin-node-resolve';
import collectSass from 'rollup-plugin-collect-sass'

export default {
  input: 'tinylibrary/static/tinylibrary/main.js',
  output: {
    name: 'tinylibrary',
    context: 'window',
    file: 'tinylibrary/static/tinylibrary/bundle.js',
    format: 'es'
  },
  plugins: [
    collectSass({}),
    resolve({})
  ],
  watch:{
    clearScreen: false
  }
};