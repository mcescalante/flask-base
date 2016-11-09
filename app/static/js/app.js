// TODO shim this properly in webpack config

// jQuery, bootstrap, tether, toastr
global.jQuery = require('jquery/dist/jquery.min.js');
window.jQuery = global.jQuery;
window.$ = global.jQuery;

window.Tether = require('tether/dist/js/tether.min.js');
require('bootstrap/dist/js/bootstrap.min.js');

window.toastr = require('toastr/build/toastr.min.js');