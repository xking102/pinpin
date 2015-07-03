var React = require('react');
var mui = require('material-ui');
var {RaisedButton} = mui;


module.exports = React.createClass({
	getInitialState:function(){
		return {
			add:false
		}
	},
	render:function(){
		console.log(this.state.add);
		var Btn = this.state.add?
            	<RaisedButton
            		label={'保存'+this.props.label}
            		secondary={true}
            		onTouchTap={this.SaveAdd}
            	/>:
            	<RaisedButton
            		label={'添加'+this.props.label}
            		primary={true}
            		onTouchTap={this.ShowAdd}
            	/>;
		return(
			<div>
				{Btn}
			</div>
		)
	},

	ShowAdd:function(){
		this.setState({
			add:true
		})
	},

	SaveAdd:function(){
		this.setState({
			add:false
		})
	},

	SaveProperty:function(){
		
	}


})
