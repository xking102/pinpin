module.exports = {
    entry : {
        index : "./index.js",
        hello : './hello.js'
    },
    output : {
        path : "./build",
        filename : "[name].js"
    },
    module : {
        loaders :[
            {test:/\.js$/, loader:'jsx-loader'}
        ]

    }
}