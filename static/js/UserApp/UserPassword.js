var React = require('react');


module.exports = React.createClass({

	render:function(){
		return (
			<div class="row-fluid">
	
	<div class="box span5">
		
		<div class="box-header" data-original-title>
			<h2>
			<i class="halflings-icon picture"></i>
			<span class="break"></span>
			基本信息
			</h2>
		</div>
		<div class="box-content">
			<div class="row-fluid">
				<row class="span4">
					<img className="grayscale" src={this.props.user.avatar} alt="Sample Image 1"/>
				</row>

				<row class="span4">
					
					<h2>{this.props.user.email}</h2>
					<h2>{this.props.user.nickname}</h2>
				</row>
			</div>
			
			
		</div>
	</div>
</div>

		)
	}
})



