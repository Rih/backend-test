const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
var webpack = require("webpack");
const path = require('path');
module.exports = {
    stats :{
        warnings: false
    },
    entry: {
        contact_index: "./ifn/static/js/components/contact_provider/index.js",
        search_index: "./ifn/static/js/components/search/index.js",
    },
    output: {
        path: path.resolve(__dirname, "./ifn/static/js"),
        filename: "[name].js",
        libraryTarget: "umd"
    },
    module: {
        rules: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        babelrc: false,
                        presets: [
                            'babel-preset-env',
                            'babel-preset-react',
                            ['es2015', {modules: false }],
                            'react',
                            'stage-0',
                          ],
                        plugins: ['babel-plugin-transform-runtime'],
                    }

                },

            },
            /*{
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        {
                            loader: "css-loader",
                            options: {
                                minimize: true
                            }
                        }
                    ]
                })
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    fallback: "style-loader",
                    use: [
                        'css-loader', 'sass-loader'
                    ]
                })

            },*/
            { test: /\.(png|woff|woff2|eot|ttf|svg)$/, loader: 'url-loader?limit=100000' }
        ],
    },
    plugins: [
        new UglifyJsPlugin({
            extractComments: true
        }),
        /*new ExtractTextPlugin('../css/[name].min.css'),*/
        new webpack.ProgressPlugin()
    ],
    externals: {
        jquery: 'jQuery'
    }


}
