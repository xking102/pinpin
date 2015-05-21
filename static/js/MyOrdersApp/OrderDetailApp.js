var React = require('react');


module.exports = React.createClass({
	contextTypes: {
    	router: React.PropTypes.func.isRequired
  	},
	render:function(){
		var params = this.context.router.getCurrentParams();
		var oid = params.oid;
		console.log(oid);
		return (
			<div className="row-fluid sortable">

				<div className="box span12">
					<div className="box-header" data-original-title>
						<h2><i className="halflings-icon user"></i><span className="break"></span>Orders</h2>	
					</div>

					<div className="box-content">
						<table className="table table-striped">
							<thead>
								<tr>
									<th>id</th>
									<th>title</th>
									<th>price</th>
									<th>Actions</th>
								</tr>
							</thead>

							<tbody>
								<div>{oid}</div>
							</tbody>

						</table>
					</div>


					
				</div>
			</div>

		)
	}
})



