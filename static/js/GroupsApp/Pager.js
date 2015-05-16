var React = require("react/addons");



module.exports = React.createClass({
	clickHandler:function(e){
		e.stopPropagation();
		this.props.listGroups();
	},
	render:function(){
		var styleObj={
			display : this.props.pager_display ? 'block':'none',
		}
		return(
			<button style={styleObj} onClick={this.clickHandler}>这里放分页</button>

		)
	}
})