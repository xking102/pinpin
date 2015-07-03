var React = require('react');
var mui = require('material-ui');
var {RaisedButton} = mui;
var PropertyApp = require('./PropertyApp');
var PropertyList = require('./PropertyList');

module.exports = React.createClass({
	getInitialState:function(){
		return {
			add:false
		}
	},
	render:function(){
		var Btn = this.state.add?
            	<RaisedButton
            		label={'就这些'+this.props.label+'吧'}
            		secondary={true}
            		onTouchTap={this.dismiss}
            	/>:
            	<div>
            	<RaisedButton
            		label={'添加'+this.props.label}
            		primary={true}
            		onTouchTap={this.show}
            	/>
            	<PropertyList label={this.props.label} list={this.props.list}/>
            	</div>;
        var PropList = this.state.add?<PropertyApp  list={this.props.list} label={this.props.label} onAdd={this.props.onAdd} />:'';
		return(
			<div className="row-fluid">
				<div className="row-fluid">{Btn}</div>

				<div className="row-fluid">{PropList}</div>

			</div>
		)
	},

	show:function(){
		this.setState({
			add:true
		})
	},

	dismiss:function(){
		this.setState({
			add:false
		})
	}


})
