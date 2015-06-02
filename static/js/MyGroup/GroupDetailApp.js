var React = require("react");
var mui = require('material-ui');
var {RaisedButton} = mui;

module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    propTypes: {
        /*
        viewMode    1 查看团员最基本信息
                    2 增加填写快递
                    3 现实快递，显示确认状况
        */
        viewMode: React.PropTypes.number,
    },
    getDefaultProps: function() {
        return {
          viewMode: 1
        }
    },
    render:function(){
        var params = this.context.router.getCurrentParams();
        var gid = params.gid;
		return(
			<div>
                {gid} {viewMode}
            </div>

		)		
	}
})