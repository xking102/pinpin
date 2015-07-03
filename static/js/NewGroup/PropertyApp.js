var React = require('react');
var mui = require('material-ui');
var {TextField} = mui;


module.exports = React.createClass({
	handelAddNew:function( e ){
		var newinput = this.refs.name.getValue();
		var newprop = {
			name:newinput
		};
		if(newinput.length>0){
			this.props.onAdd(newprop);
			this.refs.name.clearValue();
		}
		
	},
	render:function(){
		var properties = this.props.list;
		var propertyComps = properties.map(function(item){
			return <li key={item.key}>{item.name}</li>
		}.bind(this));
		return(
			<div>
			<div className="row-fluid">
				<TextField
              		ref="name"
              		style={{width:'100%'}}
              		type='text'
              		onEnterKeyDown={this.handelAddNew}
              		floatingLabelText={'输入'+this.props.label+',回车确认'}
               	/>


			</div>

			<div className="row-fluid">
				<ul>{propertyComps}</ul>

			</div>
			</div>
		)
	}

})
