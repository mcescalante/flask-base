// Import third party javascript libs here
// babel-loader is used so ES5/6, etc. should be fine
import 'bootstrap';

// Global jQuery and window config
window.jQuery = $;
window.$ = $;
window.toastr = require('toastr/build/toastr.min.js');