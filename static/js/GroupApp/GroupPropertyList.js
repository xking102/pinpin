var React = require('react');
var mui = require('material-ui');
var {Tabs, Tab} = mui;

module.exports = React.createClass({
	render:function(){
		var properties = this.props.properties;

		if(properties){
			var i = 0;
			var propComps = properties.map(function(item){
				i +=1;
				return  <Tab 
							key={i} 
							label={item}
							onActive={this._onActive}  />
		}.bind(this));
		}else {
			var propComps = null;
		}
		if(properties){
			if(properties.length){
				var title = <div><p>{this.props.label+':'}</p>
				<Tabs tabItemContainerStyle={{backgroundColor: '#3A3A3A'}} >{propComps}</Tabs></div>;
			}else{
				var title = null;
			}
		}else{
			var title = null;
		}
		return(
			<div>
			{title}
			</div>
		)
	},

	_onActive:function(tab){
		this.props.onCheck(tab.props.label);
	}
})
