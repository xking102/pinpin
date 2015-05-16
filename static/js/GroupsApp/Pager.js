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
			<button style={styleObj} disabled={this.props.query_flag} onClick={this.clickHandler}>{this.props.button_name}</button>
		)
	}
})