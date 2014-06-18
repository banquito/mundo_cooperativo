/*
 * Grunt Script for Bootstrap Stylus
 * http://gruntjs.com/
 */

'use strict';
module.exports = function(grunt) {

  grunt.initConfig({
  server: {
     port: 3000,
     base: './dist'
  },
  stylus: {
    compile: {
      options: {
        compress: false,
        paths: ['stylus'],
        urlfunc: 'embedurl', // use embedurl('test.png') in our code to trigger Data URI embedding
        use: [
          require('nib')
        ]
      },
      import: [
        'nib'
      ],
      files: [ {
        cwd: "app/assets/stylus",
        src: "*.styl",
        dest: "dist/assets/css/",
        expand: true,
        ext: ".css"
      } ]
    }
  },

  jade: {
    compile: {
      options: {
        client: false,
        pretty: true,
        data: function(dest, src) {
          var src = String(src)
            .replace("app/views", "app/models")
            .replace(".jade", ".json");
          var config = grunt.file.readJSON("app/models/_locals.json")

          if(grunt.file.exists(src)) {
            console.log(src);
            var data = grunt.file.readJSON(src);
            return { config: config, content: data } 
          }
          return { config: config } 
        }
      },
      files: [ {
        cwd: "app/views",
        src: ["**/*.jade","!_layouts/**","!**/_*.jade"],
        dest: "dist",
        expand: true,
        ext: ".html"
      } ]
    }
  },

  watch: {
    css: {
      files: ['app/assets/stylus/*.styl', 'app/assets/stylus/**/*.styl'],
      tasks: ['stylus'],
      options: {
        debounceDelay: 250
      }
    },
    views: {
      files: ['app/**/*.jade', 'app/**/*.json'],
      tasks: ['jade'],
      options: {
        debounceDelay: 250
      }
    },
    js: {
      files: ['app/assets/js/*.js', 'app/assets/js/**/*.js'],
      tasks: ['uglify'],
      options: {
        debounceDelay: 250
      }
    }
  },

  clean: {
    dist: ["dist/assets/css/*.css", "dist/assets/js/*.js"]
  },

  cssmin: {
    bootstrap: {
      files: {
        "dist/assets/css/bootstrap.min.css": ["dist/assets/css/bootstrap.css"]
      }
    },
    theme: {
      files: {
        "dist/assets/css/theme.min.css": ["dist/assets/css/theme.css"]
      }
    }
  },

  uglify: {
    dist: {
      files: {
        'dist/assets/js/bootstrap.min.js': [
            'app/assets/js/bootstrap/transition.js',
            'app/assets/js/bootstrap/alert.js',
            'app/assets/js/bootstrap/button.js',
            'app/assets/js/bootstrap/carousel.js',
            'app/assets/js/bootstrap/collapse.js',
            'app/assets/js/bootstrap/dropdown.js',
            'app/assets/js/bootstrap/modal.js',
            'app/assets/js/bootstrap/tooltip.js',
            'app/assets/js/bootstrap/popover.js',
            'app/assets/js/bootstrap/scrollspy.js',
            'app/assets/js/bootstrap/tab.js',
            'app/assets/js/bootstrap/affix.js'
        ],
        'dist/assets/js/script.js': [
          'app/assets/js/script.js'
        ]
      }

    }
  },

  });

  // Load plugins here
  grunt.loadNpmTasks('grunt-contrib-stylus');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks("grunt-contrib-jade");

  grunt.registerTask('dist', ['jade','clean','stylus', 'uglify']);
  grunt.registerTask('theme', ['stylus']);
  grunt.registerTask('build', ['jade','clean','stylus', 'uglify']);
  grunt.registerTask('server', 'Start a custom web server', function() {
      grunt.log.writeln('Started web server on port ' + grunt.config.get('server.port') );
      var base = grunt.config.get('server.base');
      var port = grunt.config.get('server.port')
      require('./app.js')
        .use("/", express.static(base))
        .listen(port);
  });
};