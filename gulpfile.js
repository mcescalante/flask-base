var gulp = require('gulp'),
    concat = require('gulp-concat'),
    scss = require('gulp-sass'),
    connect = require('gulp-connect');

var PATHS = {
  BASE: {
    CSS: 'app/static/scss/'
  },
  DEST: {
    CSS: 'app/static/css/'
  }
};

gulp.task('default', ['css', 'watch', 'connect']);

gulp.task('css', function() {
  gulp.src([PATHS.BASE.CSS + '*.scss'])
    .pipe(scss({outputStyle: 'compressed'}).on('error', scss.logError))
    .pipe(concat('style.css'))
    .pipe(gulp.dest(PATHS.DEST.CSS))
    .pipe(connect.reload());
});

gulp.task('connect', function() {
  connect.server({
    root: 'app',
    livereload: true
  });
});
 
gulp.task('html', function () {
  gulp.src('app/templates/*.html')
    .pipe(connect.reload());
});

gulp.task('watch', function() {
  gulp.watch([
    PATHS.BASE.CSS + '*.scss',
  ], ['css']);
  gulp.watch(['app/templates/*.html'], ['html']);
  gulp.watch(['app/templates/**/*.html'], ['html']);
});