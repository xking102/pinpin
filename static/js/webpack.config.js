var webpack = require('webpack');

module.exports = {
    entry : {
        index : "./index.js",
        hello : './hello.js',
        sidebar: "./sidebar.js",
        groupsindex: "./groupsindex.js"
    },
    output : {
        path : "./build",
        filename : "[name].js"
    },
    module : {
        loaders :[
            {test:/\.js$/, loader:'babel-loader'}
        ]

    },
	
	plugins: [
		new webpack.optimize.UglifyJsPlugin({
			compress: {
				warnings: false
			}
	})
		
		
	]
}