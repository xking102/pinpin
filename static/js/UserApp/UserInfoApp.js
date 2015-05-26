var React = require('react');


module.exports = React.createClass({

	render:function(){
		return (
			<div>
<div className="row-fluid">
	
	<div className="box span12">
		
		<div className="box-header" data-original-title>
			<h2>
			<i className="halflings-icon picture"></i>
			<span className="break"></span>
			基本信息
			</h2>
		</div>
		<div className="box-content">
			<div className="row-fluid">
				<row className="span4">
					<img className="grayscale" src={this.props.user.avatar} alt="Sample Image 1"/>
				</row>

				<row className="span4">
					
					<h2>{this.props.user.email}</h2>
					<h2>{this.props.user.nickname}</h2>
				</row>
			</div>
			
			
		</div>
	</div>
</div>
			</div>

		)
	}
})



