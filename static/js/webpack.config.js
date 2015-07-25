var webpack = require('webpack');
var AssetsPlugin         = require('assets-webpack-plugin');
var assetsPluginInstance = 
    new AssetsPlugin({path: './build',filename: 'react.json'});


var commonsPlugin =
    new webpack.optimize.CommonsChunkPlugin({
            name:'common',
            filename:'common.[hash].js'
        });

module.exports = {
    entry : {
        groupsindex: "./groupsindex.js",
        my_order_list:"./my_order_list.js",
        user:"./user.js",
        mygroup:"./mygroups.js",
        newgroup:"./newgroup.js"
    },
    output : {
        path : "./build",
        publicPath: "/static/js/build/",
        filename : "[name].[chunkhash].js"
    },
    plugins: [commonsPlugin,assetsPluginInstance],
    module : {
        loaders :[
            {test:/\.js$/, loader:'babel-loader?stage=1'}
        ],
        noParse: /\.min\.js/

    },


	//comppress
	// plugins: [
	// 	new webpack.optimize.UglifyJsPlugin({
	// 		compress: {
	// 			warnings: false
	// 		}
	// })

	// ]
}
