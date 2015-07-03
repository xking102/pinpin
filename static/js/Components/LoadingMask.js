var React = require('react');
var mui = require('material-ui');
var {CircularProgress} = mui;


module.exports = React.createClass({
	getInitialState:function(){
		return {
			loading:false
		}
	},
	render:function(){
		var styleObj = {
  			position: 'absolute',
  			top: '25%',
  			left: '22%',
  			width: '53%',
  			height: '49%',
  			padding: '8px',
  			zIndex: '1002',
  			overflow: 'auto',
  			marginLeft:'23%'
		};
		var mask = this.state.loading?
			<div style={styleObj}>
				<CircularProgress mode="indeterminate" />
			</div>:<div/>;
		return(
			<div>
			{mask}
			</div>
		)
	},

	show:function(){
		this.setState({
			loading:true
		})
	},

	dismiss:function(){
		this.setState({
			loading:false
		})
	}
})
