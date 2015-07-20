var webpack = require('webpack');

var commonsPlugin =
  new webpack.optimize.CommonsChunkPlugin('common.js');

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
        filename : "[name].js"
    },
    plugins: [commonsPlugin],
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
