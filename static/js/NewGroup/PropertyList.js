var React = require('react');



module.exports = React.createClass({
	render:function(){
		var properties = this.props.list;
		var propertyComps = properties.map(function(item){
			return <li key={item.key}>{item.name}</li>
		}.bind(this));
		var contents = this.props.list.length>0?
		<div><h3>{'已添加的'+this.props.label}</h3>
				<ul>{propertyComps}</ul></div>:'';
		return(
			<div style={{marginTop:'5px'}} className="row-fluid">
				{contents}
			</div>
		)
	}

})
