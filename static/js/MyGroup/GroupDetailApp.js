var React = require("react");
var mui = require('material-ui');
var {RaisedButton, Paper} = mui;

module.exports = React.createClass({
    contextTypes: {
        router: React.PropTypes.func.isRequired
    },
    render:function(){
        var params = this.context.router.getCurrentParams();
        var gid = params.gid;
		return(
			<div>
            <Paper zDepth={3}>
                {gid}
            </Paper>
            </div>

		)		
	}
})