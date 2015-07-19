var React = require('react');



module.exports = React.createClass({

	render:function(){
		var image = this.props.img+'.big.jpg'
		return(
			<a href="javascript:void(0)" onMouseEnter={this.handleChange}><img
				style={{width:'50px',height:'50px',marginRight:'5px'}}
				src={image}
			/></a>


		)
	},

	handleChange:function(e){
		this.props.ImageChange(this.props.img+'.big.jpg');
	}


})
