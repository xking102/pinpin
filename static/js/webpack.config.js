var webpack = require('webpack');

module.exports = {
    entry : {
        groupsindex: "./groupsindex.js",
        my_order_list:"./my_order_list.js"
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