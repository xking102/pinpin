var React = require('react');
var GroupImg = require('./GroupImage');

module.exports = React.createClass({
	render:function(){
		var imgs = this.props.imgs;
		if(imgs){
			var i = 0;
			var imgComps = imgs.map(function(item){
				i +=1;
				return <GroupImg 
							key={i} 
							img={item}
							ImageChange={this.props.ImageChange} 
						/>
		}.bind(this));
		}else {
			var imgComps ='';
		}
		
		return(
			<div>
			{imgComps}
			</div>
		)
	}
})
