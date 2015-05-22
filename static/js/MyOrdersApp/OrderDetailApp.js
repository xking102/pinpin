var React = require('react');


module.exports = React.createClass({
	render:function(){
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>Orders</h2>	
					</div>

					<div className="box-content">
						<div className="row-fluid">
							<div>id</div>
							<div>title</div>
							<div>price</div>
							<div>Actions</div>
								
						</div>
						<div className="row-fluid">
								<div>{this.props.oid}</div>
						</div>
						

					
					</div>


					
				</div>
			</div>

		)
	}
})



